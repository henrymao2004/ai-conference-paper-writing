# ai-conference-paper-writing

**English** | [中文](README.zh-CN.md)

A Claude Code skill that makes your AI paper read the way people naturally read: one idea per sentence, every result
with a number and a baseline, logic a reader can follow on first reading, and captions that state the finding.

I distilled it from many rounds of revising my own papers. It follows the conventions of well-written AI conference
papers and works for method, benchmark and analysis papers, and for papers that mix them.

## No AI slop

Drafts written with language models tend to share the same habits, and readers spot them at once. This skill writes
without them and flags them when it reviews your text:

| Habit | What it looks like | What the skill writes instead |
|---|---|---|
| Defensive writing | "This is not X, but Y", "We do not claim that ..." | The claim, stated positively |
| Fencing off scope | "Within the scope of this work, only under our setting ..." | One Limitations paragraph |
| Long, tangled sentences | Three clauses and four numbers in one sentence | Short sentences, one step each |
| Inserted asides | Parentheses, semicolons, dashes, ", which as noted above," | Each aside as its own sentence |
| Inflated words and jargon | delve, pivotal, nuanced, leverage, groundbreaking, vendor, render, verdict | The plain word a colleague would say |
| Stacked nouns and objects | Five new components named before any is explained, "answer verification failure rate" | One object at a time, nouns unpacked into phrases with verbs |
| Unexplained terms | An acronym or coined name used before it is explained | Every term explained in plain words at first use |
| Filler and previews | "Moreover", "It is worth noting", "In this section we first ..." | Sentences that say why the next one follows |
| Rhythm tricks | Lists of three, bold scattered in prose | Prose that stays prose |
| Unsupported claims | "significantly better", "the model wants to" | A number, a baseline, and a hedged reason |

## What you get

- **Write and revise** any section: abstract, introduction, contributions, method, benchmark construction,
  experiments, analysis, related work, limitations, discussion, captions, blog posts.
- **Structure that fits your paper.** It recognizes method, benchmark and analysis parts, picks the skeleton from the
  main contribution, and keeps each part's own conventions when they mix.
- **Findings that land.** Results come with a number and a reference point. Analysis findings set up what one would
  expect, then show what actually happens.
- **Captions and figures.** A bold finding first, then only what the reader needs to read the figure.
- **Review.** A checklist over sentences, wording, logic, figures and AI-slop patterns, with a rewrite for each hit.
- **Learn from papers you admire, if you want.** Optionally give it a few reference papers (.tex or .pdf). It splits
  them by section and paragraph, works out whether each part is method, benchmark or analysis, and writes a short
  style profile your paper then follows. Without references it uses its built-in style.

## Install

```bash
git clone https://github.com/henrymao2004/ai-conference-paper-writing ~/.claude/skills/ai-conference-paper-writing
```

Restart Claude Code. The skill loads on its own when you write or edit a paper, or call it with `/ai-conference-paper-writing`.

## Use

- "Rewrite this paragraph of my method section."
- "Tighten the introduction and check for repetition."
- "Scan my draft for AI slop."
- "Write captions for figures 2 to 4."
- "Here are three papers I like, learn their style first: a.tex, b.pdf, c.pdf."

## What's inside

| File | Covers |
|---|---|
| `SKILL.md` | Core ideas and workflow |
| `references/paper-types.md` | Method, benchmark and analysis parts, and how they combine |
| `references/sentences.md` | Sentence length, voice, clauses, numbers |
| `references/wording.md` | Concrete words, terms, citations, grounding a design in real practice |
| `references/structure.md` | Abstract, introduction, sections, paragraphs, related work, limitations, discussion |
| `references/figures.md` | Captions, labels, figures, tables |
| `references/checklist.md` | The review checklist, which also catches every habit in the table above |
| `references/learn-from-references.md`, `scripts/chunk_paper.py` | Learning from reference papers |
| `references/blog.md` | Blog posts and project pages |
