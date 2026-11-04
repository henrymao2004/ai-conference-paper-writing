# Structure: from abstract to discussion

The storyline follows the order a reader needs: motivation, what we built, how we measure, findings, explanation,
fixes. Tasks or data are designed first, and the analyses grow out of them.

## Findings

Every finding should land as a small surprise.

- Set up the expectation, then give the half that breaks it.
  - "More training data should help, yet accuracy drops on the rarest classes."
  - "Even a larger model repeats the error."
  - "A reminder in the prompt barely helps. Showing the source next to the question does."
- Headlines are vivid. Say what the subjects do the way you would tell a colleague, with a human verb and a turn:
  "The model is well aware the answer is wrong, yet writes it anyway." A flat proportion ("About half of the cases
  are classified as wrong, more than the outputs show") is a result sentence, not a headline. When the data weakens a
  vivid headline, find another vivid one that the data supports, and keep the proportion for the body.
- Headline sentences are short and put the surprising half in front. Use even, anyway, only, still. Use yet or but
  only where a turn is needed, a few times per paper.
- The same headline appears in the abstract, the bold contribution, the finding box, and the first sentence of the
  figure caption, worded the same way.
- Each finding is one comparison reported with a reference and its uncertainty. Breakdowns by condition go to
  appendix tables whose captions are findings. Do not add tests, strata or weighting the paper does not need.
- Design experiments as one coherent set. No "main result plus appendix check" side experiments.

## Abstract

- Step one level above the paper. Open with a question any reader understands, not a restatement of our setup.
- "First, ..." gives the headline answer. Then one result per further point. End with one sentence on what it means.
- No role names or coined terms that the abstract has not earned. Describe the setting once in plain words.

## Introduction

1. A concrete case a reader recognizes, ideally from human practice, in which every role appears naturally. End with
   the phenomenon in one sentence.
2. Map the case onto the studied system: the same roles, the same failure, pointing to the teaser.
3. Prior work by what it found, and what is different here. Close with the open question.
4. What we did, method only.
5. "Below, we list our main contributions and findings." Each item: a bold one-sentence claim that says what the
   finding means, then one to three sentences with method, scale, finding and a section pointer. At most one section
   pointer per item. Contributions and method stay separate.
6. One closing sentence on the significance.

Keep word counts stable when revising.

## Sections and subsections

- **Section openings** grow a question from the previous result or from a fact that does not fit: what one would
  expect, the question, then what we did to answer it.
  "The two models share the same base weights, so they should fail on the same items. The instruction-tuned model
  fails on 9 points more."
- **Subsections** relate to each other in exactly one of three ways, visible in the first sentence: a consequence, a
  rival explanation ruled out, or a follow-up on a surprise. No "Additionally" or "Moreover" lining experiments up side
  by side. The last subsection's result is the next section's question.
- **Inside a subsection**: question or aim, procedure, result with numbers and a reference, one concrete example with a
  verbatim quote, one sentence on why with its scope, a short close.
- **Ruling out an explanation**: state the explanation and the number that makes it plausible, then a comparison that
  changes only that one factor.
- **No previews or roadmaps**: no "This section first ... then ...", no "In the next two sections". Each paragraph says
  what was done and what was seen.

## Paragraphs

- One question per paragraph. Order sentences so each needs the one before.
- Vary paragraph openings: a scene, an observation with a number, a question, a fact that does not fit, an aim,
  straight into the action, a figure as subject. Neighboring paragraphs do not open the same way.
- Transitions: first, then, finally, but, however, so, taken together. Do not reuse one transition within a section.
  Empty transitions say nothing about why the next sentence follows: Moreover, Furthermore, Additionally, It is worth
  noting that, Interestingly, Notably. Drop them or name the relation.
- No rhythm tricks: lists of three when there are two or four items, the same sentence shape in every paragraph, bold
  or bullets scattered through prose. Bold is for finding sentences and defined terms.
- End on what the result means for the reader. Generic closings ("These results highlight the importance of ...",
  "This opens new avenues for future research") say nothing.
- Cut any sentence that restates an earlier sentence or paragraph. A common repeat: the first sentence of a setup
  paragraph restating the definition given one subsection earlier.

## Setup and method paragraphs

- Aim first, then the procedure. Say what stays fixed. Give a reason for the scale. No lists of variables.
- Order a setup paragraph by what the reader needs to picture it: what the items are, who is in them and what each
  does, why the key property holds, with real-world grounding, where the outcome is recorded, why it matters to the
  person who relies on it.
- Key design choices are one action sentence each, with an appendix pointer for the details.

## Results paragraphs

- The figure is the subject: "Figure 4 shows that ..." Results carry numbers with reference points.
- One verbatim example from the data makes the number concrete.
- The reason sentence is short, hedged, and scoped.

## Analogy

Use one human picture, introduced in the introduction and echoed in at most a few planned spots, such as the
definition of a concept and the last point of the discussion. Elsewhere, resonance comes from quoted model text and
the running example, never from "people do this too" in every paragraph. Sentences saying the subjects' reasons match
people's may stay, because they are findings.

## Related work

One paragraph per theme. Each work gets one sentence of what it found, then one sentence of ours. Vary sentence
shapes. No long distinctions.

## Limitations

One paragraph. Acknowledge what the result shows, state its scope, name one or two places it may not hold.

## Discussion

One opening sentence, then "First", "Second", "Finally", each looking at the findings from a different angle. Ending
on a question is fine.

## Headings

Short noun phrases, 1 to 4 words for sections and 1 to 3 for subsections, title case. Finding boxes carry the claim,
headings carry the topic.
