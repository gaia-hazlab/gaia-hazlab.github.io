# Sources and provenance

Reviewed 9 November 2026. Local repository documents establish implementation context; all SPECFEM cases and GAIA metrics in this deck remain proposals. Existing local files may contain changes beyond the listed HEAD revision, so these are provenance anchors rather than claims of a clean-checkout audit.

## Scientific and evaluation context

- Repère README: InspectAI substrate, coding-agent family, numerical checks and private-golden policy. Local repository origin: https://github.com/mdenolle/repere ; HEAD `c884108a1aff45f879b40cd9bede9251edca621f`.
- codameter README, “Choosing dv/v processing parameters”: seeded synthetic correlations, parameter-recommendation and dv/v-series evaluations. Origin: https://github.com/Denolle-Lab/codameter ; HEAD `90880884e5369342fad613acfc03e4c8f094bd16`.
- gaia-eval, `schema/SCHEMA.md`: existing task, artifact, ground-truth, provenance and rubric fields. Origin: https://github.com/mdenolle/gaia-eval ; HEAD `3303b098c8942400e122133e7fc406e1e337922b`.
- [Stanford CRFM: Language Models are Changing AI: The Need for Holistic Evaluation](https://crfm.stanford.edu/2022/11/17/helm.html), 17 November 2022. Primary source for the original seven HELM metrics and principles of broad coverage, multi-metric evaluation and standardization. Retrieved 9 November 2026. [HELM paper](https://arxiv.org/abs/2211.09110).

## Visual identity

GAIA palette and type direction come from `book/teaching/agents-intro/slides/gaia.scss` in gaia-hazlab.github.io, HEAD `89fd12148f8e8625f642ab6f4a6bcfac82ab42ec`: Husky purple #4b2e83, periwinkle #6d5bd0, lavender #f5f3fb, Inter body and Montserrat headings. The deck uses offline system fallbacks when those fonts are not installed.

`assets/gaia-logo.png` is an unmodified copy of `book/img/gaia-hazalab-logo.png` from that repository. Do not treat inclusion as permission for unrelated use of the brand.

The initial metascience teal/serif styling was replaced following the request for GAIA branding. All diagrams are editable HTML/CSS authored for this presentation.

## Illustrative material

The three dv/v samples, illustrative gates and all leaderboard values are invented. They are labeled in slides and notes. No live evaluations or SPECFEM simulations were executed for this deck. Maleen’s architecture is intentionally left for him to describe.

## Third-party runtime

Reveal.js 5.1.0 is vendored from the installed Quarto distribution. Copyright and MIT license are preserved in vendor/reveal. No external CDN, font service or runtime dependency is requested by the generated deck.
