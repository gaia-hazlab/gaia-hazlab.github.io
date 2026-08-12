# The shared rubric

Ten reviewers, one report shape. The point of a common rubric is not that everyone scores the
same — it is that when the donor and the software engineer disagree about the same page, the
disagreement is legible rather than lost in two differently-shaped documents.

## Eight dimensions

| | Dimension | The question it answers |
|---|---|---|
| **D1** | Clarity of purpose | Can I say what this project is, in one sentence, after sixty seconds? |
| **D2** | Credibility of claims | Is anything asserted that is not evidenced, dated, or falsifiable? |
| **D3** | Navigation and information scent | Could I find the one thing I came for, without guessing? |
| **D4** | Visual design and accessibility | Type, contrast, hierarchy, mobile, load time, alt text, keyboard reach. |
| **D5** | Technical depth and reproducibility | Could I actually run, install, fork, or verify something today? |
| **D6** | Governance and openness | Licence, decisions of record, who decides, what is public and what is not. |
| **D7** | Activity and durability | Is this alive, and is there reason to think it exists in three years? |
| **D8** | Relevance to me | Does this address a problem I actually have, in terms I use? |

Each persona weights these differently, and its own file gives its weights. A program officer
puts thirty points on clarity and zero on reproducibility; a research software engineer does
nearly the reverse. Both are correct for who they are.

## Severity

Severity is about consequence for **this** persona, not about how hard the fix is.

| | Meaning |
|---|---|
| **Blocker** | I stop evaluating. Whatever else is true, I do not proceed. |
| **Major** | I continue, but this materially lowers my assessment or costs me real time. |
| **Minor** | I notice it, it does not change my decision. |
| **Polish** | Craft. Worth fixing when convenient; do not let it crowd out the list above. |

A finding is only a blocker if the persona would genuinely stop. Inflating severity to get
attention destroys the value of the whole exercise — if everything is a blocker, the team
learns nothing about order of work.

## Scoring

Score each dimension 0–5.

| | |
|---|---|
| **0** | Absent |
| **1** | Present but unusable |
| **2** | Below the standard of comparable projects |
| **3** | Adequate — meets expectation, does not exceed it |
| **4** | Good — better than most comparable projects |
| **5** | Exemplary — I would point someone else at this as a model |

**3 is the honest default.** Reserve 5 for something you would actually cite as an example
elsewhere. A review where everything scores 4 or 5 is flattery, and a review where everything
scores 1 is posturing; both waste the team's time.

The weighted total is `Σ (score × weight) / 5`, giving a figure out of 100. Report the
weighted total, but lead with the findings — the number is for tracking movement across
reviews, not for judging the project.

## Evidence rules

These are not optional. They are what separates this from an opinion.

1. **Quote what you saw.** Every finding carries a verbatim quotation or a precise description
   of a visual element, with the URL it came from. No quotation, no finding.
2. **Never invent a page.** If a URL does not resolve, that is itself a finding — record the
   404 rather than reviewing the page you assumed was there.
3. **Separate observation from inference.** "The repository has no LICENSE file" is an
   observation. "The team does not care about reuse" is an inference. Mark inferences as such.
4. **Date the review.** Sites change. A finding without a date is unfalsifiable.
5. **Stay inside the persona's competence.** A program officer cannot assess whether a
   container is correctly pinned, and should not pretend to. Saying "I cannot judge this" is a
   legitimate and useful output.
6. **Note when a criticism is a matter of taste.** Reasonable people disagree about design.
   Say when you are one of them.

## Report format

Every persona produces exactly this structure, as Markdown.

```markdown
# Review: <persona title>
**Reviewed:** YYYY-MM-DD · **Scope:** <what was actually opened> · **Time spent:** <minutes>

## In one paragraph
What I concluded and what I would do next, written as this persona, in the first person.

## Weighted score: NN/100
| Dim | Score | Weight | Note |
|---|---|---|---|
| D1 Clarity of purpose | 3 | 15 | one clause |
| ... | | | |

## Findings
### 1. <short title> — BLOCKER · D6
**Where:** <URL>
**Saw:** "<verbatim quotation or precise description>"
**Why it matters to me:** <one or two sentences, in persona>
**Suggested fix:** <concrete, and small enough to actually do>
**Confidence:** high / medium / low

### 2. ...

## What worked
Two to four things done well, with the same evidence discipline. A review with no positives is
not braver, it is less useful — the team needs to know what to protect.

## What I could not judge
Things outside this persona's competence or access.

## My signature question
<the persona's own question, answered directly>
```

Order findings by severity, then by the persona's own weighting. Ten findings is a good
review; forty is a list nobody reads.
