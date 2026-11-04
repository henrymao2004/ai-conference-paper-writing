# Learning from reference papers

Authors often have papers whose writing they want to follow. Learn from them by section, then write a short style
profile that refines these rules for the current paper. The profile adds habits. It never overrides the core rules
in SKILL.md unless the author says so.

## 1. Split each reference into chunks

Run the bundled script on each reference. It accepts LaTeX source, a PDF or plain text:

```bash
python3 scripts/chunk_paper.py paper.tex --out chunks/paper.json
python3 scripts/chunk_paper.py paper.pdf --out chunks/paper.json      # needs pdftotext or pypdf
```

It writes one record per paragraph or caption with its section, its position in the section and its word count.
Read the JSON instead of the whole paper.

## 2. Label each reference and each section

- Label the paper's blocks: method, benchmark, analysis, or a mix. Label each section with the block it belongs to,
  using `references/paper-types.md`.
- A mixed paper is fine. Learn each block's habits from the sections of that block.

## 3. Extract habits, by block and by unit

For each block, note what the reference does in these units. Quote short phrases as evidence.

- **Abstract**: opening question or problem, how many results, how it ends.
- **Introduction**: paragraph sequence, where the first figure is cited, how contributions are introduced and phrased.
- **Section and subsection openings**: what the first sentence does.
- **Paragraph moves**: the order of question, procedure, result, example and reason.
- **Results sentences**: how numbers and references are written, how uncertainty is reported.
- **Captions**: structure, length, what the first sentence says.
- **Tables and figures**: chart types, how comparisons are laid out.
- **Recurring phrases** for transitions, claims and hedges.
- **Length**: words per section and per paragraph.

## 4. Write the profile

Save it next to the paper, for example `style-profile.md`:

```markdown
# Style profile: <paper or venue>
References: <titles>, blocks: <method | benchmark | analysis per reference>

## Habits to follow
- <unit>: <habit>, as in "<short quote>" (<reference>, <section>)

## Where the references differ from the core rules
- <habit> ... follow the references | keep the core rule (author decides)

## Length targets
- Abstract ~N words, introduction ~N words, captions ~N words
```

Show the profile to the author before using it. When a reference habit conflicts with a core rule, list it under
"Where the references differ" and ask which to keep.

## 5. Use it

When writing a section, read the profile's habits for that block and unit together with the core rules. When the
author later corrects a habit, update the profile.

## Copyright

Learn structure and habits. Quote only short phrases as evidence, and never copy a reference's sentences into the new
paper.
