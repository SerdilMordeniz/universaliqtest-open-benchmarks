# Three AI models on 40 visual reasoning questions

Preliminary report | 14 November 2026 | https://www.universaliqtest.com/ai-iq-test

An exploratory report on accuracy, completion, API latency and cost. One 40-question run per model, with separate development checks showing how reasoning limits and response delivery affected completion.

## Original 40-question run

Medium reasoning; 8,192 output tokens including reasoning; one run per dated model. Six slots exhausted the output allowance. These figures describe the declared settings and cannot establish a general intelligence ranking.

| Model | Correct / 40 | Wrong returned | Cutoffs | Valid / 40 | Median API time | API usage |
| --- | --- | --- | --- | --- | --- | --- |
| Gemini 4 Carbon | 34/40 (85%) | 1 | 5 | 35/40 | 13.9 s | $0.921820 |
| Claude Fable 5.2 | 32/40 (80%) | 7 | 1 | 39/40 | 4.0 s | $1.759680 |
| GPT-6 Astra | 37/40 (92.5%) | 3 | 0 | 40/40 | 3.7 s | $1.796600 |

Cutoffs count as unsuccessful in the original score and remain distinct from wrong returned answers. Every final question-slot duration was recorded. One additional unanswered HTTP 503 took 29.516 seconds, was unbilled, and was retried identically. No returned answer or cutoff was repeated in that scored run.

Each model received the same figures, eight numbered options and strict JSON prompt in a fresh context. Display labels followed the frozen balanced schedule. The visual content was the public test content, rendered into static 1152-by-1552 images; the interactive human experience was not reproduced. Scores were checked offline against the private production grading key.

## Separate development checks

Positions 24, 28, 35, 36, 38 and 40 were selected because at least one model had exhausted the original limit on each. They were used to investigate completion and resources, without accuracy grading. Valid means a complete schema-valid response; it does not mean correct.

| Profile | Output ceiling | Valid / 6 | Cutoffs | Unavailable | API usage |
| --- | --- | --- | --- | --- | --- |
| GPT-6 Astra; OpenAI; reasoning response excluded | 32,768 | 6/6 | 0 | 0 | $1.083305 |
| Claude Fable 5.2; Anthropic; reasoning response excluded | 32,768 | 6/6 | 0 | 0 | $0.801520 |
| Gemini 4 Carbon; Google AI Studio; reasoning response excluded | 32,768 | 3/6 | 1 | 2 | $1.046414 |
| Gemini 4 Carbon; Google Vertex global; reasoning response excluded | 65,536 | 3/6 | 0 | 3 | $0.493298 |
| Gemini 4 Carbon; Google Vertex global; reasoning response included_then_discarded | 65,536 | 6/6 | 0 | 0 | $1.419026 |

All development profiles used high reasoning. The initial Carbon profile also had an earlier unanswered, unbilled timeout whose single recovery succeeded; the failure remains in the measurements. Later profiles remain separate. No new answer replaces an earlier score.

With API reasoning progress requested and its text discarded locally, the final Carbon profile completed all six selected questions. One question used 51,145 output tokens in 656.051 seconds. Another completed in 403.480 seconds; both exceeded the earlier five-minute timeout boundary. This supports a working delivery/allowance approach for these development items, without proving general reliability or a universal timeout cause.

## Interpretation

One 40-item pass cannot establish a stable intelligence ranking. Output budgets affected completion. The medium/high labels have provider-specific meanings, and equal token ceilings do not imply equal compute. API duration includes network, queueing and generation; it is not isolated thinking time or human active answering time. The later calibration has different settings and collection conditions and is not a latency ranking.

On the post-hoc 34 questions with valid answers from all three models, Carbon and Astra each scored 33/34 and Fable 30/34. That subset excludes capped questions after observing failures; it is a sensitivity check, not an unbiased replacement ranking or evidence of equivalence.

The source items are public and training contamination was not assessed. We operate the source test and conducted this internal exploratory evaluation; external peer review has not been performed. No human IQ or percentile was measured or assigned to a model.

Original full run: $4.478100. Development checks: $4.843563. Earlier technical pilots: $0.334781. Total reported API usage: $9.656444. Receipts reconciled against billing. Fees and taxes excluded.

## Reproducibility and citation

UniversalIQTest.com (2026). Three AI models on 40 visual reasoning questions: preliminary report. 14 November 2026. https://www.universaliqtest.com/ai-iq-test

Downloads include aggregate results, per-item measurements, methods and file hashes. Individual solutions, the private grading key, participant records, credentials and reasoning text are not included.

- [OpenRouter: reasoning tokens and output limits](https://openrouter.ai/docs/guides/best-practices/reasoning-tokens)
- [OECD: human-oriented tests as measures of artificial intelligence](https://www.oecd.org/en/publications/ai-and-the-future-of-skills-volume-1_5ee71f34-en/full-report/using-human-skills-taxonomies-and-tests-as-measures-of-artificial-intelligence_06d3b428.html)
