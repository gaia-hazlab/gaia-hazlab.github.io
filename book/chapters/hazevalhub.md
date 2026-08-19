# HazEvalHub

## Overview

The HazEvalHub is where hazard models get scored. It holds the metrics, the validation
protocols, and the held-out data that decide whether a prediction is good enough to act on.

We are developing two tracks for evaluating model performance:
- **Extreme event monitoring**: classification, regression, segmentation (e.g., detection of landslides, floods, earthquakes)
- **Surrogate of Physical Models** trained on physics-based simulations, a framework based on the AI Institute for Dynamical System Common Task Framework (collab with Nathan Kutz and Kaggle) with fair evaluation and hidden data set.
- **Leaderboard**: a set of hazard-relevant evaluation metrics when using geospatial and terrestrial networks in collaboration with AI2.

## 🔴 Live prototype — FrugalMind EvalHub

> **[▶ Open the live eval board](https://mdenolle.github.io/frugalmind)**

**FrugalMind EvalHub is the first working prototype of HazEvalHub.** It is a live
evaluation board for scientific AI agents in geoscience, and it establishes the design
the full HazEvalHub generalizes to hazard tasks.

Every submission is scored on three questions:

| Question | What it measures |
|---|---|
| **Is it right?** | Accuracy against ground truth |
| **What did it cost?** | Token/dollar cost — cost is a *first-class* axis, not an afterthought |
| **Is it reproducible?** | Deterministic scoring from declarative JSON specs, so results can't be gamed |

**The board.** A cost-versus-performance scatter: each model appears twice — *without*
domain skills (hollow marker) and *with* them (filled) — joined by a line showing the
**skill lift**. Systems in the upper-left (high performance, low cost) win. Hover for
model version, weights, and exact metrics; export to CSV/PNG.

**Tasks.** Document-based (literature review, retrieval-augmented QA, multimodal
interpretation), software-agent (writing a detector, executing a pipeline, producing
data), and research-workflow (orchestration and trajectory scoring). Concrete benchmarks
include *dv/v* parameter choice, STA/LTA code generation, and ObsPy function usage.
Validation splits are public; **test splits are hidden** to prevent memorization.

**An early result.** Free *local* 7B models (`qwen2.5:7b`, `llama3.1:8b`) reach perfect
scores on configuration tasks once given domain skills — but fail at numerical code
generation, where only cloud models succeed (~0.56 base, rising to 0.76 with skills).
Domain skills lift small, cheap models to frontier parity on some task classes and not
others; knowing *which* is the point of the board.

**Where it goes next.** Adopt its JSON scoring spec as the shared `gaia-eval` scorecard
schema, carry the cost/frugality axis into the hazard metrics below, and extend the task
taxonomy from agent tasks to the full pillar × hazard grid — keeping the agent tasks as
the "research-workflow" track.

## Evaluation Framework (TBD)

### Components

1. **Performance Metrics**: Standardized metrics for model evaluation
2. **Validation Protocols**: Rigorous testing procedures
3. **Benchmarking**: Comparison against established baselines
4. **Uncertainty Quantification**: Assessment of prediction confidence
5. **Operational Testing**: Real-world performance evaluation

## Evaluation Metrics
<!--
### Classification Metrics

For hazard presence/absence classification:

```python
from gaia_hazlab.evaluation import ClassificationMetrics

# Calculate metrics
metrics = ClassificationMetrics(y_true, y_pred)
print(f"Accuracy: {metrics.accuracy()}")
print(f"F1 Score: {metrics.f1_score()}")
print(f"ROC-AUC: {metrics.roc_auc()}")
```

### Regression Metrics

For continuous hazard intensity prediction:

```python
from gaia_hazlab.evaluation import RegressionMetrics

# Evaluate predictions
metrics = RegressionMetrics(y_true, y_pred)
print(f"RMSE: {metrics.rmse()}")
print(f"MAE: {metrics.mae()}")
print(f"R²: {metrics.r_squared()}")
```

### Spatial Metrics

For spatially-explicit hazard mapping:

```python
from gaia_hazlab.evaluation import SpatialMetrics

# Calculate spatial agreement
metrics = SpatialMetrics(reference_map, predicted_map)
print(f"IoU: {metrics.iou()}")
print(f"Dice: {metrics.dice_coefficient()}")
print(f"Spatial Correlation: {metrics.spatial_correlation()}")
``` -->

## Validation Protocols

### Cross-Validation

#### Temporal Cross-Validation

For time-dependent hazard data:
<!--
```python
from gaia_hazlab.evaluation import TemporalCV

cv = TemporalCV(n_splits=5)
for train_idx, test_idx in cv.split(data, time_variable='date'):
    # Train and evaluate model
    pass
``` -->

#### Spatial Cross-Validation

For spatially-correlated data.

<!-- ```python
from gaia_hazlab.evaluation import SpatialCV

cv = SpatialCV(n_splits=5, buffer_distance=1000)
for train_idx, test_idx in cv.split(data, coordinates=coords):
    # Train and evaluate model
    pass
``` -->

### Hold-out Testing

- Geographic hold-out: Testing on different regions
- Temporal hold-out: Testing on future time periods
- Event-based hold-out: Testing on specific hazard events

## Benchmarking

### Baseline Models

We will provide standard baselines for comparison (e.g., statistical baselines, classic ML models).

### Performance Comparison
<!--
```python
from gaia_hazlab.evaluation import BenchmarkSuite

# Run benchmarking
benchmark = BenchmarkSuite()
benchmark.add_model('your_model', your_model)
benchmark.add_baseline('persistence', persistence_model)
benchmark.add_baseline('historical_avg', avg_model)

results = benchmark.evaluate(test_data)
benchmark.plot_comparison()
``` -->

## Uncertainty Quantification

<!-- ### Prediction Intervals

Quantify prediction uncertainty:

```python
from gaia_hazlab.evaluation import UncertaintyQuantifier

uq = UncertaintyQuantifier(model)
predictions, lower_bound, upper_bound = uq.predict_with_intervals(X_test)
``` -->

### Probabilistic Evaluation

<!-- Assess calibration of probabilistic predictions:

```python
from gaia_hazlab.evaluation import CalibrationAnalysis

calibration = CalibrationAnalysis(y_true, y_prob)
calibration.plot_reliability_diagram()
print(f"Brier Score: {calibration.brier_score()}")
``` -->

## Case Studies

<!-- ### Example: Flood Model Evaluation

```python
from gaia_hazlab.evaluation import FloodModelEvaluator

# Load test data
test_events = load_flood_events('historical_floods.csv')

# Evaluate model
evaluator = FloodModelEvaluator(model)
results = evaluator.evaluate_events(test_events)

# Generate report
evaluator.generate_report('flood_model_evaluation.html')
```

## Evaluation Reports

### Automated Reporting

Generate comprehensive evaluation reports:

```python
from gaia_hazlab.evaluation import EvaluationReport

report = EvaluationReport()
report.add_metrics(metrics_dict)
report.add_plots(figures)
report.add_summary(description)
report.export('evaluation_report.html')
```

### Report Contents

Standard reports include:
- Executive summary
- Performance metrics tables
- Visualization of predictions vs. observations
- Error analysis and diagnostic plots
- Uncertainty assessment
- Recommendations for improvement -->

## Quality Assurance

### Model Validation Checklist

Before deployment, models must pass:

- [ ] Cross-validation on training data
- [ ] Hold-out test performance meets thresholds
- [ ] Spatial/temporal generalization verified
- [ ] Uncertainty properly quantified
- [ ] Edge cases and failure modes identified
- [ ] Computational efficiency acceptable
- [ ] Documentation complete

## Operational Evaluation

### Real-time Monitoring
<!--
Monitor deployed model performance:

```python
from gaia_hazlab.evaluation import PerformanceMonitor

monitor = PerformanceMonitor(model)
monitor.track_predictions(live_data)
monitor.alert_if_drift(threshold=0.1)
``` -->

### Feedback Integration

- Collect user feedback on predictions
- Incorporate new observations for continuous evaluation
- Update models based on operational experience

## Evaluation Standards

We follow established standards:

- **WMO Guidelines**: For meteorological hazards
- **USGS Standards**: For seismic hazards
- **ISO Standards**: For risk assessment
- **ML Best Practices**: For model evaluation

## Contributing

Help improve our evaluation framework:

1. Suggest new metrics for specific hazard types
2. Contribute validation datasets
3. Share evaluation protocols from your research
4. Report issues or limitations

## Resources

- [Metrics API Reference]({{ github_org_url }}/{{ book_repo }}/wiki/metrics-api)
- Validation Datasets

## Future Developments

Planned enhancements:
- Automated model selection based on evaluation metrics
- Multi-model ensembling with performance-weighted aggregation
- Continual learning with online evaluation
- Explainable AI techniques for model interpretability
