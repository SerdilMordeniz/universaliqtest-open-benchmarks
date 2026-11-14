# Release changes

## 2026-11-14

This release supersedes the October snapshot as the primary download and applies the current production methodology. The October version remains available at https://doi.org/10.5281/zenodo.24216588.

| Topic | 10 October 2026 | 14 November 2026 |
| --- | --- | --- |
| Counting basis | Earlier all-recorded and screening rules | Current first-recorded-exposure reference cohort, then quality screening |
| Headline totals | 334,915 recorded; 109,433 screened | 216,773 included; 94,224 passing checks |
| Group mean | Transform of the mean stored percentile | Arithmetic mean of individually transformed midpoint percentiles |
| Interval spread | IQR-derived estimate | Sample standard deviation of individual transformed scores |
| Capture | Separate public HTTP requests | One read-only repeatable-read production snapshot |
| Aggregate rows | 501 | 482 |
| Reproduction evidence | Published values and interval arithmetic | Published values, exported sample SD and aggregate score moments |

The revised counting and scoring rules were introduced on 10 November 2026 and applied retrospectively. Differences between these releases combine a policy change and a later capture date. Subtracting the totals does not measure test traffic, participant loss or the number excluded by one particular rule.

All existing public CSV fields are retained. `stddevIQ` is added to the ten CSVs. Source records, test questions, credentials and internal diagnostic signals are not part of this release. The technical review does not establish independent psychometric validation.
