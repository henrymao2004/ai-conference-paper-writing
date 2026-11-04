# Paper types and how they combine

Most AI conference papers are built from up to three blocks. Decide which blocks a paper has and which one is the
main contribution. The main block sets the skeleton and the headline. The other blocks become sections inside it and
keep their own writing rules.

| Paper | Main block | Usual extra blocks |
|---|---|---|
| Method or algorithm | Method | Analysis of why it works, sometimes a new evaluation set |
| Benchmark or dataset | Benchmark | Analysis of what models get wrong, sometimes a baseline method |
| Analysis or empirical study | Analysis | A test set built for the study, sometimes a fix that works |

## Method block

**Skeleton**: problem and why current methods fall short, method, properties or theory, experimental setup, main
results, ablations, analysis.

- **Problem first.** Open with the task, the setting a reader recognizes, and the concrete failure of existing
  methods, with a number if you have one.
- **Intuition before formulas.** Each component: one sentence of what it does and why, then the formula or algorithm.
  A figure of the pipeline helps more than a long paragraph.
- **Mechanism is the content here.** Describe every step a reader needs to reimplement it. Leave project plumbing,
  logging and engineering detail to the appendix or code.
- **Notation once.** Define each symbol at first use, keep it fixed, and collect it in a table if there are many.
- **Theory.** State the meaning in one plain sentence, then the theorem, then what it implies for practice. Proofs go
  to the appendix.
- **Main results.** One table or figure against strong baselines on standard benchmarks. Lead with the claim: "Our
  method improves accuracy over the strongest baseline on all five tasks, by 4.2 points on average." Report seeds or
  confidence intervals the field expects.
- **Ablations.** Each row removes or changes one component and the text says what that component contributes.
- **Headlines** state the gain plainly. The surprise style is for the analysis parts.

## Benchmark block

**Skeleton**: what capability is untested and why it matters, task definition, data construction, quality control,
metrics, evaluated systems, results, analysis of failures.

- **The gap in evaluation.** Name the capability and show that existing benchmarks miss it with a concrete example.
- **Task definition.** What an instance is, what the system sees, what it must output, and how it is scored.
- **Construction.** Where the data comes from, how items are generated or collected, how difficulty is controlled, and
  how leakage and shortcuts are prevented. This is the core of the paper, so describe it fully.
- **Realism.** When an item mirrors real practice, say what ours does and cite the real systems or sources it follows.
- **Quality control.** Annotation process, agreement, filtering, each in action sentences with appendix pointers.
- **Metrics.** Why this metric measures the capability, in one or two sentences.
- **Results.** A leaderboard table, then the findings it supports. "Even the strongest model solves 31% of items."
- **Failure analysis** follows the analysis block.

## Analysis block

**Skeleton**: a question grown from an observation, the setup, findings in order of surprise, explanation, a fix if
there is one.

- **Each finding is a surprise.** Set up the expectation, then give the half that breaks it, with a number and a
  reference.
- **One comparison per finding**, with its uncertainty. Breakdowns go to appendix tables.
- **Subsections relate** as a consequence, a rival explanation ruled out, or a follow-up on a surprise.
- **Describe behavior, not tooling.** What the subjects read, did and wrote.
- **One verbatim example** per finding makes the number concrete.

## Combining blocks

- **Method plus analysis**: results first prove the method works, then analysis sections ask why. Analysis headlines
  may use the surprise style. Keep the method's headline plain.
- **Benchmark plus analysis**: the leaderboard comes first, then analysis sections explain what models get wrong. The
  benchmark's construction section should be complete enough that the analysis needs no new setup.
- **Analysis plus a fix**: the fix is one section near the end, written like a small method block with its own
  baseline comparison.
- **Introduction**: contributions list one item per block, main block first.
- **One storyline**: each extra block answers a question the previous section raised. Avoid sections that sit side by
  side with no stated relation.
