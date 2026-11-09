# Proposed GAIA evaluation metrics

Discussion proposals, not implemented benchmark specifications. HELM motivates coverage, multiple metrics and standardized comparison. It evaluates language models; GAIA will evaluate whole agent systems. Its seven original dimensions are accuracy, calibration, robustness, fairness, bias, toxicity and efficiency. Our simulation-specific measures are an adaptation, not official HELM metrics.

Source: [Stanford CRFM, HELM introduction (2022)](https://crfm.stanford.edu/2022/11/17/helm.html).

| Dimension | Measurement | Required agreement |
|---|---|---|
| Scientific correctness | Passing simulation attempts / scheduled simulation attempts; per-receiver waveform errors | Mandatory checks, tolerances, units, reference, attempt and failure policy |
| Numerical agreement | Relative L2 error `norm(pred-ref)/norm(ref)` per receiver on a fixed grid | Separate absolute-error rule for near-zero references; alignment and components; no hidden rescaling |
| Robustness | Difference in pass rates on paired original and scientifically equivalent reworded tasks | Pairing, allowed changes, baseline rate and variant rate |
| Generalization | Pass counts by new physical setup or case family | Held-out source/receiver/model families; avoid near-duplicate leakage |
| Agent repeatability | Success fraction across repeated agent runs, per case | Number of runs, model settings, budgets; repeats are clustered by case |
| Artifact reproducibility | Independent reruns that satisfy the scientific checks / attempted reruns | Environment, commands, input hashes, replay access; distinguish from rerunning the agent |
| Clarification sensitivity | Correctly flagged incomplete tasks / incomplete tasks | Expert label of whether clarification was necessary |
| False alarms | Complete valid tasks incorrectly blocked / complete valid tasks | Reviewed clean controls; report with sensitivity |
| Confidence calibration | Brier score and reliability diagram when predeclared probabilities exist | Confidence target, outcome label, sufficient observations, confidence recorded before scoring |
| Efficiency | Elapsed time, model API spend, CPU/GPU hours per attempt | Include failed attempts, hardware, timeout, API price date and caching; separate cost categories |
| Coverage gaps | Explicit list of untested regimes and metric dimensions | Scope and why omitted; do not rename regime coverage as demographic fairness |

## Before evaluating

Choose one variant and a reviewed fixture. Declare expected output artifacts and version the scorer. Use deterministic numerical checks when appropriate; use expert-reviewed rubrics for open-ended clarification. An LLM judge requires validation against human labels.

Use scientific correctness and output completeness as explicit gates. Show efficiency beside them rather than averaging inexpensive failures into a supposedly good overall score. Avoid a universal composite until the group agrees on the decision it represents.

For missing outputs, wrong units, non-finite values and timeouts, specify how an attempt fails. Identify infrastructure incidents separately, preserve original records and declare a rerun policy before evaluation. Never silently drop failed cases from the denominator.

## Calibration is not clarification

A model can request missing information without reporting meaningful probabilities. Calibration requires a clearly defined forecast, such as “probability that this artifact passes the fixed scientific checks,” and labeled outcomes over many attempts. Numerical uncertainty intervals are another target with their own coverage tests.

## A real leaderboard needs provenance

Record task-set version and split, scorer revision, system and model revision, prompt/skill revision, allowed tools, environment and hardware, resource limits, repeats, failure policy, and cost accounting. Separate simulation, diagnosis and clarification suites. Publish counts, per-case failures and uncertainty; do not imply that 9/10 reliably outranks 8/10.

Where suitable, include a fixed transparent-script baseline. Distinguish a whole-system comparison from a controlled experiment about a model or skill. Keep hidden references outside the agent’s access and outside the public presentation repository.
