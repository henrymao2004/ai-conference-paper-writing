---
name: ai-conference-paper-writing
description: A writing style for AI conference papers (NeurIPS, ICML, ICLR, ACL, CVPR and similar) and their blog posts or project pages, covering method/algorithm, benchmark/dataset and analysis papers and papers that mix them. Use it whenever you draft, revise, restructure, shorten or review any part of a paper - abstract, introduction, contributions, method, dataset or benchmark construction, experiments, results, ablations, analysis, related work, limitations, discussion, figure and table captions, figure labels - or a blog post about a paper. Also use it to learn the style of reference papers the user supplies, and whenever the user asks to "polish", "reorganize", "tighten", "make it read better", "check for repetition", "write the caption", or pastes a paragraph that reads badly, even if they never mention style.
---

# AI conference paper writing

A writing style for AI conference papers, distilled from many rounds of revision. It aims at prose that reads the way
people naturally read: a reader follows every sentence on first reading and leaves each section knowing one new thing.
Apply it to text you write and to text you are asked to fix.

When the author writes the body prose and asks you to fix a paragraph, change only that paragraph, keep its sentences
where they work, and list what you changed. When a section has no prose yet and the author did not ask for a draft,
leave a `% Paragraph to write:` comment with the content it should carry.

## The core idea

1. **Describe the object, concretely.** Write what is studied, built or measured in the words you would use with a
   colleague. Avoid abstractions, metaphors and coined labels.
2. **One step per sentence.** Each sentence does one thing: what we did, what we saw, or what it means.
3. **Results carry numbers and a reference.** Every result names its baseline or reference point. Findings in
   analysis set up the expectation, then give the half that breaks it.
4. **Logic you can see.** Order sentences so each needs the one before. Each paragraph, subsection and section has one
   visible relation to what came before.
5. **Say it once.** No sentence restates an earlier one. No previews of what is coming.

## Workflow

1. **Identify the paper's blocks.** Most AI papers combine up to three kinds of contribution: a method or algorithm, a
   benchmark or dataset, and an analysis of behavior. Decide which the paper has and which one is the main
   contribution. Read `references/paper-types.md` for how each block is written and how blocks combine.
2. **Optional: if the author supplies reference papers**, learn from them first with `references/learn-from-references.md`
   and `scripts/chunk_paper.py`. Their habits refine these rules for this paper. Without references, the rules here are the whole style.
3. **Write or revise** with `references/sentences.md` and `references/wording.md`, plus:
   - abstract, introduction, contributions, sections, paragraphs, related work, limitations, discussion:
     `references/structure.md`
   - figures, tables, captions, labels, finding boxes: `references/figures.md`
   - blog posts and project pages: `references/blog.md`
4. **Review** with `references/checklist.md`, which also catches the habits of model-written text: defensive lines,
   scope fences, tangled sentences, asides, inflated words, stacked nouns, unexplained terms, filler. Report each
   hit with the sentence and a rewrite. Run it on every draft you produce, including your own.

When you change text, show the new text and one line per change. Do not lecture the author on the rules.

## Rules readers notice first

- **No semicolons, no parentheses** in prose, captions included, except to define an acronym or a short label at its
  first use, as in "Over-Correction Rate (OCR)". No appositives or comma-enclosed asides. Write figure references as
  sentences: "Figure 2 shows ...". Math and citations are exempt.
- **No "not X but Y"** and no defensive contrasts ("rather than", "instead of"). State claims positively.
- **Write the object, not the tooling.** Analysis and benchmark prose says what the subjects see and do. Method prose
  explains the method itself in full, but leaves out how the project's code, logging or infrastructure works.
- **Concrete over abstract.** "the summary keeps the number but drops its unit" over "an information gap".
- **Cite by stating the finding.** "Doe et al. found that ...". "See" points only to your own figures and sections.
- **Ground design choices in real practice, ours first.** Say what our setup does, then name the real systems that do
  the same, one citation each. The citations carry the realism. Never announce that the purpose is realism.
- **Short captions.** A bold finding, at most one or two sentences needed to read the figure, then the uncertainty and
  its n.
- **Short headings.** Noun phrases of 1 to 4 words for sections and 1 to 3 for subsections, in title case.
