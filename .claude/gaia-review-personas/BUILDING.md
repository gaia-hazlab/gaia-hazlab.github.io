# Regenerating the personas

The ten `SKILL.md` files are generated, not hand-edited. Every shared section — the report
format, the evidence rules, the closing instructions — is identical across all ten because it
comes from one template. Editing a generated file directly means the next regeneration silently
reverts you.

```bash
python3 build.py     # rewrites personas/ and shared/ ; leaves examples/ alone
```

- **`spec.py`** holds what differs between personas: identity, context, the ordered checks,
  disqualifiers, vocabulary limits, weights, signature question. Edit here.
- **`build.py`** holds what is shared: the rubric, the method, the synthesis guide, and the
  template each persona is poured into. Edit here to change all ten at once.

`spec.py` asserts on import that there are ten personas and that each one's weights sum to 100
across the eight dimensions. A bad edit fails loudly rather than producing a skewed rubric.

`examples/` is hand-written and survives regeneration deliberately — reviews are dated
observations and should not be regenerated.
