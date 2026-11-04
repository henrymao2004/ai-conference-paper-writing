# Wording, terms and citations

## Write the actual thing

Describe what the subjects literally see, read, write or receive. A reader should be able to picture it.

- Write "the summary keeps the number but drops its unit", "the model answers before it reads the table", "every
  answer names the passage it used".
- Avoid abstractions and metaphors: gap, boundary, blank, slot, guarantee, true state, link by link, chain of trust,
  locus, pipeline of failure.
- Avoid engineering descriptions in prose: null, status fields, flags, "reads the config file", log formats, proxy
  behavior, what fields a reply contains, when exactly a failure happens inside the system.
- Avoid project-internal ids and codes outside example spots. Ids, ticket numbers and file names belong only in a
  running example, a teaser, a case box, or quoted model text.
- Avoid job titles that add nothing. Write the role that matters, such as "the person who signs off", unless the title is the point.
- Write consequences, not the obvious. Do not stop at "the output alone cannot tell whether it is right". Write what
  follows: "every later step builds on it".

## Describe the object, not the tooling

A paper describes what is studied: the tasks, roles, inputs, model settings, judging. How the project's code,
logging or infrastructure works goes to the repository docs.

Before adding a setup sentence, ask whether a reader needs it to understand what the subjects see or how results are
measured. If not, leave it out.

Examples that justify a design must be concrete and recognizable. "as people do when a form is processed later"
means nothing to a reader. "as a patient who books a blood test gets a booking number before any result" does.

## Describe procedures directly

Say who receives what and produces what: "We give each model the passage the annotator saw and ask it to write
the label." Do not coin labels for procedures or conditions ("replay", "clean trajectories", "cell A",
"prompt-side fix"). Controls are stated as what was run: "To test whether X, we run the same items with the correct
answer in the context. Models change a correct answer in 2% of runs, Appendix C." The name of a control lives in the appendix.

## Plain words

- Use the plain word a colleague would say. Inflated vocabulary reads as filler: delve, intricate, pivotal, nuanced,
  underscore, landscape, tapestry, realm, leverage, utilize, facilitate, holistic, seamless, paradigm, multifaceted.
  So does hype: groundbreaking, remarkable, unprecedented, revolutionary, a significant step forward, paves the way.
- Avoid engineering and business jargon in prose, the words of tickets and dashboards: vendor, render, verdict,
  surface (as a verb), signal (as a verb), artifact, operationalize, stakeholder, granular, instance-level,
  end-to-end, out of the box. Write the everyday word: company or developer for vendor, write or show for render,
  label, judgment or decision for verdict.
- Introduce objects one at a time. Do not stack several new roles, components or conditions in one sentence, and do
  not pile nouns into one compound. Unpack a noun pile into a phrase with a verb.
- Explain every term, acronym and symbol in plain words at its first use.

## Concepts and names

- Keep the number of named concepts small. Introduce each inside a narrative sentence, the way "these opening
  tokens, i.e., token cues" does. Never "we call this X" or "X is Y" as a bare definition.
- A new concept should arrive after the reader has seen the thing it names, ideally in a concrete case first.
- One name per thing for the whole paper. If a measure has a name, use the name only in its definition, axis labels,
  legends and table headers. Body sentences say what was counted: "62% of answers copy the wrong
  number".
- Ordinary verbs stay ordinary. Do not turn a plain verb into a defined term.
- When a concept later splits into parts, introduce it first as one idea so the split comes as a surprise.
- For model internals, state what the model marks or represents, never "knows" or "believes", unless the author chose
  a specific phrasing for a headline.
- Explain a method name once, where the method is introduced.

## Citations

- Cite by stating the finding: "Doe et al. found that larger models recall rarer facts." Never "see Doe et al." for outside work. "See" is only for your own figures, sections and appendices.
- Related work is assertive: per work, one short line of what it studies or found, then our line. No fine-grained
  defensive distinctions, no "complementary", no "a careful reading is needed".
- When a prior concept only looks related, state its setting plainly first and let our sentence state ours.

## Grounding a design in real practice

When a design choice mirrors how real systems or people behave, make that visible through the citations, without
saying "for realism".

1. Say what our setup does first.
2. Then say the real systems do the same, naming them, one citation per example.
3. Cite the standard or documentation that makes the general point.

Example:

> Our simulated lab returns each test result two days after the order and shows the order as open until then.
> Hospital labs report on a similar schedule \citep{a}, and patient portals show an order as pending until its result
> arrives \citep{b}.

Keep the exact wording of a general claim faithful to the source. Prefer "most results arrive within two days" over an
absolute such as "results always arrive in two days" when the source gives a range.

Real incidents that show the phenomenon in the wild belong in the introduction, as a cited example.

## No defensive lines

Write the claim and stop. Lines that only fence off scope ("within the scope of this work", "only in our setting",
"we limit ourselves to") go to one Limitations paragraph.

State what was done. A selection step is one action sentence with an appendix pointer: "We discard runs where the
model never produced an answer, Appendix G." Statements such as "X is used only for evaluation" go to the appendix.
Scope statements belong in Limitations. Do not add judge-vs-judge agreement or other reassurance unless the author
asks for it.
