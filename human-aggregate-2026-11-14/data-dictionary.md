# Data dictionary

Each row is a group aggregate. CSVs use UTF-8, decimal points and LF line endings. An empty numeric cell means unavailable.

| Field | Definition |
| --- | --- |
| countryCode | Source country label. Legacy labels are retained; validate codes before mapping to an ISO geography. |
| ageCategory; ageRange | Youth 12–18, Young Adult 19–35, Adult 36–65, Senior 66–100. |
| gender | Supported published self-reported categories: male/female. |
| educationLevel; studyArea | Normalized categories used by the live statistics; missing or unsupported categories are omitted. |
| n | Age-group count in the selected view. |
| validatedN | Group records in the current reference cohort passing the quality checks. The field name is historical and does not imply psychometric validation. |
| allN | Group records included in the current reference cohort before the quality-pass filter. It excludes recognised repeats, uncertain identity matches, unverifiable responses and test data. It is not all submitted attempts. |
| validationRate | `100 * validatedN / allN`, rounded to one decimal. |
| meanIQ | Arithmetic mean of individual transformed midpoint percentiles, rounded to one decimal. |
| stddevIQ | Sample standard deviation of those individual transformed scores, rounded to one decimal; unavailable for n <= 1. Added to support reproduction. |
| p10; p25; p50/median; p75; p90 | The corresponding group percentile in percentile-rank space, linearly interpolated and transformed to the score scale. Age uses p50; other dimensions use median. |
| ciLower; ciUpper | `meanIQ +/- 1.96 * stddevIQ / sqrt(n)` using the published rounded mean and SD. Unavailable for n <= 1 or missing SD. Age files omit these fields. |
| avgTimeMs; meanTimeMs | Average recorded total time in milliseconds; age uses meanTimeMs. |
| updatedAt | Latest included submission in the group, rather than the capture timestamp. |

Individual score transformation is `100 + 15 * Phi^-1(p)` after clamping p to 0.0001–0.9999. Equal raw scores share midpoint percentiles; response speed does not break score ties. Country, education and study-area summaries use age-normalized percentiles. Age and default gender summaries use global percentiles. The all-included and quality-screened views use their respective reference distributions.

`score-moments.json` stores group n, the sum of unrounded transformed scores and the sum of their squares. Reproduce the rounded mean as `round(scoreSum/n, 1)` and the rounded sample SD as `round(sqrt((scoreSquaredSum-scoreSum^2/n)/(n-1)), 1)`. This is aggregate evidence; it does not contain participant rows or verify the original answers.

Counts differ by dimension because missing or unsupported categories are excluded. Refer to the coverage table in README.md and exact schemas in manifest.json. A larger voluntary sample does not remove selection bias. These approximate intervals omit normalization uncertainty, test measurement error and selection bias, and do not establish representative population coverage.
