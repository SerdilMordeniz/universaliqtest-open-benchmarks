# Technical methodology review — 14 November 2026

This review covers the current-policy aggregate snapshot captured at 2026-11-14 09:40:28.956 UTC. It checks production-source agreement, coherent denominators, file integrity, score arithmetic and figure interpretation.

## Capture and reconciliation

All ten aggregate tables and the headline denominator were captured in one read-only repeatable-read production transaction. The source was the same first-recorded-exposure reference used by the live statistics. Its latest included submission was 2026-11-14 01:57:24.926 UTC.

The source contained **216,773 included tests and 94,224 passing current quality checks**. These agree with the live overview at capture. Country, gender, education and study-area totals are lower because their supported categories do not cover every included record. Age totals reconcile exactly. The dimension counts are listed in README.md and verification.json.

The release contains 482 aggregate rows. A field-by-field comparison with all ten live CSV exports matched every row. The release adds the sample SD as stddevIQ and group score moments for verification. All CSV byte lengths, schemas and SHA-256 hashes are recorded in manifest.json.

## Current policy and the historical break

The first-recorded-exposure and revised screening policy was introduced on 10 November 2026. Recognised repeats, uncertain identity matches, unverifiable responses and test data are outside the current reference cohort. The passing-quality view is a subset of that cohort. Browser and historical identity evidence cannot certify unique humans, and unrecognised prior exposure remains possible.

The October snapshot reported **334,915 recorded tests and 109,433 quality-screened results under the earlier rules**. Its larger totals are historical observations from a different cohort definition. They are not a current participant count or a directly comparable growth baseline. CHANGELOG.md describes the break; the original version remains available at https://doi.org/10.5281/zenodo.24216588.

## Mean, dispersion and intervals

Each stored midpoint percentile is clamped to 0.0001–0.9999 and transformed through the inverse normal distribution with location 100 and scale 15. The group mean is the arithmetic mean of these individual values; the spread is their sample standard deviation. Both are rounded to one decimal, as in the current website implementation.

Country, education and study-area summaries use age-normalized percentiles. Age and default gender summaries use global percentiles. Each view uses its own reference distribution. Group quantiles are transformed after linear interpolation in percentile space.

All **482 means and sample SDs** reproduce from the published aggregate score sums and squared sums. All **474 screening rates** reproduce from the group counts. The **437 available approximate intervals** reproduce as `meanIQ +/- 1.96 * stddevIQ / sqrt(n)`. Age charts display the interquartile range and do not present it as a confidence interval.

The technical checks establish arithmetic agreement with the documented implementation. The approximate intervals omit selection bias, normalization uncertainty and measurement error. Their population coverage has not been established.

## Figures and supported use

The seven figures use the frozen verified inputs and carry the capture date. Country figures show sample sizes and are ordered by country code. The selected-country display threshold is 200 passing records. Screening percentages use included reference-cohort tests as their denominator. Age figures show middle-50% ranges and mean individual scores.

This release supports descriptive analysis and teaching about a self-selected online cohort. An independent external psychometric assessment has not been performed. Item discrimination, internal consistency, retest stability, clinical validity and representative population IQ norms are outside the evidence supplied here.
