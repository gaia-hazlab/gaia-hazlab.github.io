#!/usr/bin/env python3
"""Offline teaching example. Invented data and thresholds, no agent run."""
import json
import math

TRUTH = [0.0020, 0.0020, 0.0020]
ESTIMATES = [0.0018, 0.0021, 0.0019]
VALID = [True, True, True]

def score(truth, estimates, valid):
    if not truth or not (len(truth) == len(estimates) == len(valid)):
        raise ValueError('Nonempty, equally sized series required')
    if not all(type(v) is bool for v in valid):
        raise ValueError('Validity mask must contain booleans')
    if not all(math.isfinite(v) for v in truth + estimates):
        raise ValueError('Non-finite samples are invalid outputs')
    coverage = sum(valid) / len(truth)
    errors = [abs(a-b) for a,b,v in zip(truth, estimates, valid) if v]
    mae = sum(errors) / len(errors) if errors else None
    return {'illustrative_only': True, 'mae_fractional_dvv': mae,
            'valid_coverage': coverage,
            'passed': mae is not None and mae <= 0.0002 and coverage >= 0.90}

if __name__ == '__main__':
    print(json.dumps(score(TRUTH, ESTIMATES, VALID), indent=2))
