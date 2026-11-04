# Sentences

## One step per sentence

Each sentence advances one step: what was done, what was seen, or what it means. Two parallel findings are two
sentences. In English aim for 12 to 30 words and split anything over about 35. In Chinese aim for 15 to 40 characters
and split anything over 50.

## Subjects

- "We" for what the authors did: "We give each model the same passage."
- The studied subjects for behavior: the model, participants, annotators, the system.
- The measure for numbers: "The rate falls from 62% to 18%."
- The figure for figure results: "Figure 3 shows ...". Never "this paper" as subject, never a section number as the
  subject of a sentence.

## Active voice, plain verbs

- Active voice. Avoid "Asked afterwards, ...", "what it is handed", "is shown to be".
- Plain verbs: compare, test, ask, read, replace, split, falls to, rises to, copies, fills in. Avoid perform, conduct,
  achieve, demonstrate, reveal, leverage, utilize, showcase.
- Natural collocations. Avoid stiff phrases such as "in plain view", "change their story", "write a result in",
  "the very reasons".

## Clauses

- At most one subordinate clause per sentence. At most one "To ...", "If ...", "When ..." in front.
- Few "that" and "who" relative clauses. Turn them into a second sentence.
- No appositives (", the model that wrote the draft,") and no comma-enclosed asides. Make them their own sentence:
  "This model wrote the draft."
- No semicolons. No parentheses except at the definition of an acronym or a short label: "An evidence rule (I1)".
  Math, citations and LaTeX are exempt.
- No em dashes used as asides either. An aside that matters becomes its own sentence. One that does not is cut.
- Ranges as "from X to Y". Panels as "Panel a shows ...".

## Positive statements

- No "not X but Y", "rather than", "instead of", "is not ... it is ...", "X ≠ Y". Write the claim positively.
  - "The saved note, not the new request, decides the answer" becomes "The answer follows the saved note over the new
    request".
  - "a strong instruction not to save" becomes "a strong instruction against saving".
- No pre-emptive denials: "We do not claim that ...", "This does not mean ...". Move scope to Limitations.
- One hedge at most, only where the data is uncertain. Not "may potentially suggest".
- Plain factual negation of data is fine: "No annotator opened the source."

## Numbers

- A change gives start and end: "falls from 62% to 18%".
- A comparison names its reference: "against 41% without the reminder".
- At most two numbers per sentence.
- Use one precision consistently and follow the paper's existing convention.
- When a sample is small, write the count: "in 9 of 30 runs".
- No vague quantities: various, numerous, several, substantially, significant without a test. Give the number.

## Endings

- Each result paragraph ends with a short sentence that says what it means and how far it reaches.
- Reason sentences only claim what the data supports. Use "may" or "likely" and do not invent motives for the subjects,
  as in "the model wants to".

## Examples

| Before | After |
|---|---|
| We conduct an analysis of the errors (Figure 3), which reveals that retrieval is the locus of the failure. | We read every wrong answer. Most come from a wrong retrieved passage, as Figure 3 shows. |
| The model does not answer the question but instead copies the context. | The model copies the context. |
| It is the prompt, not the model size, that drives the effect. | The prompt drives the effect more than model size does. |
| Annotators, who saw only the title, labeled each item; they then rated their confidence. | Annotators saw only the title. They labeled each item and rated their confidence. |
