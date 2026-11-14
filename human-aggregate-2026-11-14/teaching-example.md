# Reading the current-cohort aggregates

## Group differences and individual spread

The quality-screened age table reports a mean of 103.2 for ages 19–35 and 98.0 for ages 36–65: a difference of 5.2 scale points. Their middle-50% ranges are 92.4–113.5 and 86.8–108.1. The overlap is 92.4–108.1, spanning 15.7 points.

Draw the two ranges and explain why a group mean does not predict an individual's score. These bars are interquartile ranges. Their overlap is not a hypothesis test. The groups are cross-sectional age bands, rather than repeated measurements of one person.

## Choose the correct denominator

Portugal has 333 passing records among 665 included reference-cohort tests: `333/665*100 = 50.1%` after rounding. Poland has 2,518 among 5,687: `2518/5687*100 = 44.3%`.

These denominators already exclude the record classes outside the current reference cohort. They are not all attempts submitted to the website. Compare the definitions with the October release before comparing percentages across versions.

## Reproduce the current interval

Select a country row with n greater than one. Use validatedN for the passing view and allN for the all-included view. Calculate `1.96*stddevIQ/sqrt(n)` and add/subtract the result from meanIQ. Then find the same group in score-moments.json and independently reconstruct the rounded mean and sample SD.

Explain which uncertainties this arithmetic omits: selection bias, measurement error, normalization uncertainty and unrecorded prior exposure. A narrow interval does not make an online sample representative of a national population.

All inputs are aggregate records from the frozen CSVs and score-moments.json. The manifest records the capture and checksums. No participant-level rows are provided.
