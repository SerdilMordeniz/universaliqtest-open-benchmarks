# UniversalIQTest aggregate snapshot — 14 November 2026

Version **2026-11-14**, captured **2026-11-14 09:40:28.956 UTC**. Publisher and rights holder: **UniversalIQTest**. Licensed under **CC BY 4.0**.

The snapshot contains **216,773 tests included in the current reference cohort**, of which **94,224 passed the current quality checks**. These totals matched the live statistics at capture. The latest included submission was recorded at **2026-11-14 01:57:24.926 UTC**. Later live totals can change as the reference data refreshes.

The ten CSVs contain **482 aggregate group rows** across country, age band, gender, education and study area, in quality-screened and all-included views. They were generated from one read-only, repeatable-read production snapshot using the same aggregate calculations as the website. The public CSV fields were compared with all ten live exports: all 482 rows matched. This release adds `stddevIQ` and aggregate score moments for reproducible arithmetic.

## Counting basis

The reference cohort follows the first-recorded-exposure policy introduced on **10 November 2026**. Recognised repeat attempts, uncertain identity matches, unverifiable responses and test data are excluded before the current cohort is counted. The screened view then selects the included records passing the quality checks. These counts do not certify unique individuals or psychometric validity.

The [10 October snapshot](https://doi.org/10.5281/zenodo.24216588) used the earlier counting and scoring rules and reported 334,915 recorded tests and 109,433 quality-screened results. Its larger historical totals are not a growth baseline for the current cohort. See [CHANGELOG.md](CHANGELOG.md).

## Dimension coverage

| Dimension | All included | Passed quality checks |
| --- | ---: | ---: |
| Entire reference cohort | 216,773 | 94,224 |
| Country | 216,556 | 94,092 |
| Age | 216,773 | 94,224 |
| Gender | 215,647 | 93,763 |
| Education level | 215,251 | 93,604 |
| Study area | 213,317 | 92,737 |

Missing or unsupported categories explain dimension-specific coverage. Supported gender rows are male/female. Education and study-area categories use the live normalization and exclusions. Country tables retain source labels, including legacy labels that should not automatically be treated as valid ISO codes. These totals are not interchangeable denominators.

## Files and verification

- [manifest.json](manifest.json): capture scope, policy description, source commit, schemas and CSV SHA-256 hashes.
- [overview-evidence.json](overview-evidence.json): coherent cohort counts, capture time and latest included submission.
- [data-dictionary.md](data-dictionary.md): definitions and interpretation.
- [methodology-review.md](methodology-review.md): completed technical review and evidence limits.
- [score-moments.json](score-moments.json): group counts, score sums and squared-score sums; no participant identifiers or individual rows.
- [verification.json](verification.json): checks for 482 rows and score moments, 474 screening rates and 437 approximate intervals.
- [live-comparison.json](live-comparison.json): comparison with all ten public CSV exports at capture.
- `charts/`: seven figures, each in PNG/SVG/PDF with alternative text.
- [teaching-example.md](teaching-example.md): worked exercises using this release.

## Reproduction

From the unpacked release root:

```text
node scripts/verify-dataset-release.mjs .
python scripts/render-dataset-charts.py .
```

Verification uses Node.js 22 or later and built-in modules. Rendering uses Python 3 and Matplotlib; versions are recorded in `charts/runtime.json`. The capture helper included with the parser can retrieve independently cached public exports, but does not recreate this coherent production snapshot or its score-moment evidence. A future production capture needs its own recorded cutoff, policy and review.

## Licence and citation

Copyright © 2026 UniversalIQTest. The aggregate CSVs, figures, release documentation, aggregate score moments and standalone reproduction scripts distributed here are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). See [LICENSE](LICENSE). Credit UniversalIQTest, link to the licence and identify changes.

> UniversalIQTest (2026). *Online matrix-reasoning test performance: aggregate snapshot, 14 November 2026* (version 2026-11-14). https://doi.org/10.5281/zenodo.24217581. CC BY 4.0.

An independent external psychometric assessment has not been performed. The results describe a self-selected online cohort. Population inference, clinical assessment, test reliability and causal interpretations require additional evidence.

Live sources: https://www.universaliqtest.com/statistics and https://www.universaliqtest.com/methodology-and-limits.

Archived version https://doi.org/10.5281/zenodo.24217581
