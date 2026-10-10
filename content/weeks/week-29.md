---
layout: week
week: 29
permalink: /weeks/week-29/
title: Model evaluation
description: “The loss went down” is a useful observation, but it does not answer
  whether the model performs the task better.
summary: “The loss went down” is a useful observation, but it does not answer whether
  the model performs the task better.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 29
kicker_secondary: Optional · 8 hours
---

## Start with the problem

“The loss went down” is a useful observation, but it does not answer whether the model performs the task better. Evaluate likelihood, task outcomes and evidence use separately, with a simple baseline that can expose unnecessary modeling complexity.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Give every metric a clear denominator

**Think about this first.** Should a two-token batch and a twenty-token batch have equal weight?

For aggregate language-model loss, sum negative log-likelihood over evaluated tokens and divide by the number of evaluated tokens. Perplexity is the exponential of that mean. Averaging batch perplexities or unweighted batch means generally gives a different, misleading result.

Tokenizer, corpus, context window, masking and stride affect the metric. Compare like-for-like evaluations and exclude padding/ignored targets consistently. Perplexity measures the token prediction objective under those conditions; it is not a universal measure of answer usefulness or truthfulness.

## 2. Compare systems under one task contract

**Think about this first.** What changed besides the model weights?

Compare base, prompted base, tuned model and a retrieval-assisted system while keeping task labels and the comparison purpose explicit. Prompted base versus tuned under the same template isolates adaptation better than comparing a raw continuation prompt to a carefully designed tuned prompt.

For classification, include invalid outputs in the denominator and inspect per-class errors. Macro F1 gives classes equal weight under the stated missing-class convention. Exact match is suitable for fixed labels or narrow extraction; natural-language answers need a reviewed equivalence policy. Do not repair malformed outputs invisibly before scoring.

## 3. Evaluate evidence and practical significance

**Think about this first.** Can a fluent answer with a real citation still be wrong?

Yes. Check that each claim follows from its specific source revision and answers the actual question. RAG with current evidence and a closed-book model have different information access; explain what that comparison measures. Test missing, irrelevant and stale context instead of only ideal retrieval.

Human or LLM judgments need a rubric, sample count and disagreement handling. Pairwise order can bias ratings. Semantic or word-overlap scores can miss changed numbers and conditions. Report uncertainty and resource cost alongside quality, and avoid selecting a configuration on a repeatedly inspected final test.

## Walk through one case

Suppose NLL means are 1 over two tokens and 3 over eight. The aggregate mean is (2×1 + 8×3)/10 = 2.6, not 2. Perplexity is exp(2.6). Separately, a model predicting one label for every three-class example can have perfect format but poor class coverage. Neither observation establishes successful adaptation.

## Guided practice

1. Freeze the task contract, sources and final evaluation split.
2. Evaluate prompted base, tuned and a simple deterministic baseline using identical labels.
3. Calculate token-weighted NLL/perplexity under one declared tokenizer/masking policy.
4. Report per-class errors, invalid outputs, unsupported claims and resources.
5. Inspect paired failures and make a retain/reject decision. If results guide further tuning, reserve a new untouched final test before claiming final performance.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Explain calibration versus ranking, exact match versus semantic similarity, and likelihood versus task correctness. Discuss judge bias, paired evaluations and practical effect size. SHAP can describe a model's feature attribution under assumptions; it does not prove a causal explanation. Keep attribution and business causality separate.

## Knowledge check

1. How do you aggregate token loss?
2. What happens to invalid model outputs?
3. Why use a simple baseline?
4. Can the test set guide endless tuning?

### Answer key

1. Sum evaluated NLL and divide by total evaluated tokens before exponentiating.
2. They remain task failures in the all-attempt denominator.
3. It reveals whether the model adds value beyond a cheaper transparent rule.
4. Doing so consumes its independence; use fresh final cases afterward.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 30: Serving and documentation](/weeks/week-30/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [Perplexity of fixed-length models](https://huggingface.co/docs/transformers/perplexity)
- [Classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)
