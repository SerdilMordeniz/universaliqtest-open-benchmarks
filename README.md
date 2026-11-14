# UniversalIQTest Open Aggregates & AI Visual Reasoning Measurements

Open, machine-readable artifacts published by [UniversalIQTest.com](https://www.universaliqtest.com):

1. **Preliminary AI Visual Reasoning Report (14 November 2026):**
   - Live report (29 languages): https://www.universaliqtest.com/ai-iq-test
   - Aggregate results (`results.json`), 120 per-item API timings & token counts (`measurements.json`), and protocol settings (`methods.json`).
2. **Human Participant Aggregate Snapshot (Version 2026-11-14, CC BY 4.0):**
   - Zenodo DOI: https://doi.org/10.5281/zenodo.24217581
   - Kaggle reproducible notebook: https://www.kaggle.com/code/universaliqtest/reading-the-universaliqtest-aggregate-data
   - Live statistics & methodology: https://www.universaliqtest.com/dataset-overview-and-sources and https://www.universaliqtest.com/methodology-and-limits

All human figures describe a self-selected online cohort (216,773 included attempts, 94,224 passing current quality checks) and do not represent national population IQ or clinical psychometric norms. AI results report raw accuracy, completion, latency, and API cost without assigning human IQ scores to models.

## Files

- [AI report and public measurements](ai-visual-reasoning-2026-11-14/): seven files mirrored byte-for-byte from the published website, including the figure and SHA-256 manifest. The 120 baseline question slots involved 121 API requests because one unanswered HTTP 503 was retried. Separate ungraded development profiles are retained in the measurements.
- [Frozen human aggregate release](human-aggregate-2026-11-14/): the original 57-file November release, including ten CSV tables, aggregate score moments, seven figures and standalone reproduction scripts.
- [Companion manifest](companion-manifest.json): file lengths and SHA-256 hashes for the mirrored artifacts.

## Verification and reproduction

Run `node verify-artifacts.cjs` from the repository root to verify all mirrored files without an API key, database connection or paid model requests.

To reproduce the human aggregate arithmetic, run `node human-aggregate-2026-11-14/scripts/verify-dataset-release.mjs human-aggregate-2026-11-14`. The snapshot README documents chart reproduction and counting rules.

The AI files support inspection of reported outcomes and collection conditions. Individual solutions, private grading keys, participant records, credentials and reasoning text are omitted. This repository does not independently reproduce private-key grading or provide a new full model evaluation. The study is preliminary, internally checked and has not undergone external peer review. Provider routes and allowances changed during selected-item development, so those observations do not isolate a universal timeout cause.

## Citation and licensing

Study: UniversalIQTest.com (2026). *Three AI models on 40 visual reasoning questions: preliminary report*. 14 November 2026. https://www.universaliqtest.com/ai-iq-test

Human snapshot: UniversalIQTest (2026). *Online matrix-reasoning test performance: aggregate snapshot, 14 November 2026*, version 2026-11-14. https://doi.org/10.5281/zenodo.24217581. The snapshot retains its original [CC BY 4.0 licence](human-aggregate-2026-11-14/LICENSE). Its totals use the policy introduced on 10 November and are not directly comparable with the earlier October release.
