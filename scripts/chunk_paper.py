#!/usr/bin/env python3
"""Split a paper into section-labelled paragraphs and captions, for learning its writing habits.

Input: LaTeX source (.tex), a PDF (needs the `pdftotext` command or the pypdf package) or plain text (.txt, .md).
Output: JSON, a list of records {"section", "subsection", "kind", "index", "words", "text"}, where kind is
"paragraph", "caption" or "abstract", and index counts paragraphs within the section.

Usage:
  python3 chunk_paper.py paper.tex --out chunks.json
  python3 chunk_paper.py paper.pdf --out chunks.json
  python3 chunk_paper.py paper.tex --summary          # one line per section: paragraphs and words
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys


def read_tex(path, seen=None):
    """The LaTeX source with \\input and \\include files inlined and comments removed."""
    seen = seen or set()
    path = os.path.abspath(path)
    if path in seen or not os.path.exists(path):
        return ""
    seen.add(path)
    text = open(path, encoding="utf-8", errors="ignore").read()
    text = re.sub(r"(?<!\\)%.*", "", text)
    base = os.path.dirname(path)

    def inline(m):
        name = m.group(2)
        name = name if name.endswith(".tex") else name + ".tex"
        return read_tex(os.path.join(base, name), seen)
    return re.sub(r"\\(input|include)\{([^}]*)\}", inline, text)


def braced(text, start):
    """The content of the brace group opening at text[start] and the index after it."""
    depth, i = 0, start
    while i < len(text):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    return text[start + 1:], len(text)


def plain(tex):
    """LaTeX to readable text: commands with text arguments keep the text, math and refs become placeholders."""
    t = re.sub(r"\\(cite[tp]?|citep|citet|citeauthor)\*?(\[[^\]]*\])*\{[^}]*\}", "[cite]", tex)
    t = re.sub(r"\\(ref|cref|Cref|autoref|eqref)\{[^}]*\}", "[ref]", t)
    t = re.sub(r"\\label\{[^}]*\}", "", t)
    t = re.sub(r"\$\$.*?\$\$|\\\[.*?\\\]", " [math] ", t, flags=re.S)
    t = re.sub(r"\$[^$]*\$", "[math]", t)
    for _ in range(3):
        t = re.sub(r"\\(textbf|textit|emph|underline|texttt|textsc|mbox|text)\{([^{}]*)\}", r"\2", t)
    t = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", t)
    t = t.replace("{", "").replace("}", "").replace("~", " ")
    return re.sub(r"\s+", " ", t).strip()


def chunk_tex(text):
    out, section, subsection = [], "Front matter", ""
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", text, re.S)
    if m:
        out.append(dict(section="Abstract", subsection="", kind="abstract", text=plain(m.group(1))))
        text = text[:m.start()] + text[m.end():]
    body = text.split("\\begin{document}", 1)[-1]
    # captions first, removed from the body
    for m in list(re.finditer(r"\\caption\*?(\[[^\]]*\])?\{", body)):
        cap, _ = braced(body, m.end() - 1)
        out.append(dict(section="", subsection="", kind="caption", text=plain(cap), _pos=m.start()))
    body = re.sub(r"\\begin\{(figure|table|figure\*|table\*|algorithm)\}.*?\\end\{\1\}", "\n\n", body, flags=re.S)
    tokens = re.split(r"(\\(?:section|subsection|paragraph)\*?\{[^}]*\})", body)
    caps = [r for r in out if r["kind"] == "caption"]
    out = [r for r in out if r["kind"] != "caption"]
    for tok in tokens:
        h = re.match(r"\\(section|subsection|paragraph)\*?\{([^}]*)\}", tok)
        if h:
            if h.group(1) == "section":
                section, subsection = plain(h.group(2)), ""
            elif h.group(1) == "subsection":
                subsection = plain(h.group(2))
            else:
                out.append(dict(section=section, subsection=subsection, kind="paragraph_heading",
                                text=plain(h.group(2))))
            continue
        for para in re.split(r"\n\s*\n", tok):
            p = plain(para)
            if len(p.split()) >= 8:
                out.append(dict(section=section, subsection=subsection, kind="paragraph", text=p))
    # captions: attach to the section whose text precedes them in document order
    for c in caps:
        c.pop("_pos", None)
        c["section"] = "Figures and tables"
    return out + caps


def pdf_text(path):
    if shutil.which("pdftotext"):
        return subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True).stdout
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("Reading a PDF needs the pdftotext command or the pypdf package (pip install pypdf).")
    return "\n\n".join(page.extract_text() or "" for page in PdfReader(path).pages)


HEADING = re.compile(r"^\s*(\d+(\.\d+)*|[A-H](\.\d+)*)\.?\s+([A-Z][A-Za-z0-9 ,:&\-]{2,60})\s*$")
BACK = re.compile(r"^\s*(References|Bibliography|Acknowledge?ments?|Appendix|Appendices)\s*$", re.I)


def chunk_plain(text):
    out, section, subsection = [], "Front matter", ""
    text = re.sub(r"-\n(\w)", r"\1", text)
    lines = text.splitlines()
    buf = []

    def flush():
        p = re.sub(r"\s+", " ", " ".join(buf)).strip()
        if len(p.split()) >= 8:
            kind = "caption" if re.match(r"(Figure|Fig\.|Table)\s*\d+[:.]", p) else "paragraph"
            out.append(dict(section="Abstract" if section == "Abstract" else section, subsection=subsection,
                            kind="abstract" if section == "Abstract" else kind, text=p))
        buf.clear()
    for line in lines:
        s = line.strip()
        if re.fullmatch(r"(?i)abstract", s):
            flush()
            section = "Abstract"
            continue
        if BACK.match(line):
            flush()
            section, subsection = s.title(), ""
            continue
        h = HEADING.match(line)
        if h and len(s.split()) <= 8:
            flush()
            num, title = h.group(1), h.group(4).strip()
            if num[0].isalpha():
                section, subsection = ("Appendix " + num + " " + title, "") if "." not in num else (section, title)
            elif "." in num:
                subsection = title
            else:
                section, subsection = title, ""
            continue
        if not s:
            flush()
        else:
            buf.append(s)
    flush()
    return out


def main():
    ap = argparse.ArgumentParser(description="Split a paper into section-labelled paragraphs and captions.")
    ap.add_argument("paper", help=".tex, .pdf, .txt or .md")
    ap.add_argument("--out", help="JSON output path (default: print)")
    ap.add_argument("--summary", action="store_true", help="print paragraphs and words per section")
    a = ap.parse_args()
    ext = os.path.splitext(a.paper)[1].lower()
    if ext == ".tex":
        rows = chunk_tex(read_tex(a.paper))
    elif ext == ".pdf":
        rows = chunk_plain(pdf_text(a.paper))
    else:
        rows = chunk_plain(open(a.paper, encoding="utf-8", errors="ignore").read())
    counts = {}
    for r in rows:
        key = (r["section"], r["kind"])
        counts[key] = counts.get(key, 0) + 1
        r["index"] = counts[key]
        r["words"] = len(r["text"].split())
    if a.summary:
        seen = {}
        for r in rows:
            s = seen.setdefault(r["section"], [0, 0])
            s[0] += 1
            s[1] += r["words"]
        for name, (n, w) in seen.items():
            print(f"{name[:50]:50s} {n:4d} chunks {w:6d} words")
        return
    data = json.dumps(rows, ensure_ascii=False, indent=1)
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        open(a.out, "w", encoding="utf-8").write(data)
        print(f"wrote {len(rows)} chunks to {a.out}")
    else:
        print(data)


if __name__ == "__main__":
    main()
