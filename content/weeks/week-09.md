---
layout: week
week: 9
permalink: /weeks/week-09/
title: RAG evaluation fundamentals
description: A good demonstration shows that your system can succeed.
summary: A good demonstration shows that your system can succeed.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 9
kicker_secondary: 8 hours
---

## Start with the problem

A good demonstration shows that your system can succeed. An evaluation reveals when it fails. Build a small, versioned set whose source evidence you can inspect, then use it to locate the first broken stage rather than awarding one vague “quality” score.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Label the business question

**Think about this first.** What is correct when an approval date is missing?

A refusal to invent the date can be the correct answer. Label expected outcome, relevant sources, required claims and acceptable citations before running the system. Include answerable, ambiguous, conflicting and insufficient-evidence cases. Keep a reference to the exact source revision.

Relevant sources may be alternatives, while required sources may form a conjunction. Either of two clauses may establish general terms; a schedule row and its controlling section may both be required. Represent those relationships separately. Keep paraphrases from the same document or scenario in one split so near-duplicates do not inflate held-out results.

## 2. Measure each boundary

**Think about this first.** Can a correct-looking answer hide poor retrieval?

Yes: it might come from model memory, a lucky guess or leaked reference text. Check parsing, chunk completeness, candidate retrieval, final ranking, context evidence, claim support and task correctness separately. A parser can corrupt a unit before a retriever ever sees it. A good ranking can still lose the crucial condition during packing.

Precision@k counts relevant results among k slots; state how short lists are handled. Recall@k divides retrieved relevant IDs by all labeled relevant IDs. Reciprocal rank is the inverse position of the first relevant item; MRR averages it across questions. NDCG uses graded relevance and rank discounts relative to an ideal ordering. State the gain and discount conventions.

## 3. Keep judging and uncertainty visible

**Think about this first.** Can a faithful quotation be the wrong answer?

An Atlas payment clause can be quoted perfectly in response to a Beacon question. Support and task correctness are different checks. Exact match works for narrow labels or quotes but can reject valid paraphrases. Semantic similarity can tolerate dangerous changes to numbers or negation. An LLM judge needs a written rubric and assessment against reviewed examples; model preference is not ground truth.

Retain failed requests in the denominator. Show sample counts and family slices alongside averages. Do not repeatedly tune on the test set. Use development data for selection and reserve fresh cases for a final comparison. Small synthetic sets are diagnostic evidence, not production-accuracy estimates.

## Walk through one case

Suppose the result list is [wrong, right] at cutoff three, with one relevant source. Under a fixed-cutoff convention, precision is 1/3, recall is 1 and reciprocal rank is 1/2. Now suppose the answer omits “after inspection approval.” Retrieval metrics can remain unchanged while correctness falls. This tells you to inspect context and generation, not just increase top-k.

## Guided practice

1. Author approximately thirty questions with IDs, source revisions, expected outcomes and required claims.
2. Keep document/scenario families together when dividing development and held-out cases.
3. Run one baseline and one controlled change on the same corpus. Store candidates, context, answer, status, latency and configuration.
4. Calculate one ranking result by hand and reconcile it with your code. Mark metrics not applicable when no relevant answer evidence exists.
5. Review one failure from each stage. Count crashes, inappropriate abstentions and unsupported answers separately while retaining every attempt.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Classification precision/recall differ from retrieval metrics in their unit of counting. PR curves help inspect positive-class performance under imbalance; ROC uses true-positive and false-positive rates. Threshold selection needs task costs and validation. Calibration asks whether predicted probabilities match observed frequencies; a retrieval similarity score is not automatically calibrated. Grouped or time-aware validation should match the deployment situation.

## Knowledge check

1. Why separate source relevance from required evidence?
2. What is RR for a first hit at rank four?
3. Why count failed requests?
4. Can an LLM judge replace labels without validation?

### Answer key

1. Alternatives can independently support an answer, while a linked relationship may require several sources together.
2. One quarter; MRR is the average over evaluated questions.
3. Removing difficult failures makes the system appear artificially better.
4. No. Its rubric, bias and disagreement behavior need assessment.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 10: Observability and tracing](/weeks/week-10/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [Ranked retrieval evaluation](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html)
- [Probability calibration](https://scikit-learn.org/stable/modules/calibration.html)
