---
layout: week
week: 18
permalink: /weeks/week-18/
title: Agent evaluation
description: An agent writes a plausible final answer after several invalid tool calls.
summary: An agent writes a plausible final answer after several invalid tool calls.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 18
kicker_secondary: 8 hours
---

## Start with the problem

An agent writes a plausible final answer after several invalid tool calls. Scoring only the final text rewards behavior you would not deploy. Evaluate both the user outcome and the important execution constraints, while allowing more than one legitimate route to success.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Define success and prohibited behavior

**Think about this first.** Must every correct run use exactly the same tool sequence?

Usually not. A case may be solvable through several valid routes. Label the required outcome, supporting evidence, allowed effects and constraints rather than one rigid golden transcript. Exact trajectories are useful only when sequence itself is part of the contract.

Record attempted calls, validated calls, observations, artifacts and effects. Distinguish a proposed write from an actual committed write. Include denied scope, missing evidence, conflicting sources, tool failure and stale approval cases. An unsafe successful-looking answer should not pass merely because its wording matches a reference.

## 2. Keep stochastic failures measurable

**Think about this first.** What does one successful run establish?

It establishes that the system succeeded once under those conditions. Repeated runs can expose model variability, but repeated trials of the same case are not new independent business scenarios. Report cases, repeats and aggregation separately.

Use fixed source and tool fixtures for reproducible regression tests, then add real-boundary integration checks. Mock external services where appropriate, not the agent logic you intend to evaluate. Track overall success and constraint violations, plus error slices and resource distributions. Keep exceptions and incomplete runs in the denominator.

## 3. Connect offline metrics to business value

**Think about this first.** Could higher offline accuracy still disappoint users?

Yes. A slower answer may arrive after a decision, or a model may improve easy cases while missing costly ones. Define task outcomes, correction burden and guardrail metrics with stakeholders. Online experiments need a meaningful assignment unit and controls for repeated users or shared documents.

Predefine the comparison and avoid repeatedly peeking until a result looks favorable. A p-value is not the probability that a system is useful, and statistical significance does not establish practical importance. Small pilots should be described with their sample size, uncertainty and operational limits.

## Walk through one case

An evaluation asks for a local draft, forbids sending and requires evidence from an authorized contract. One run produces a correct draft after attempting an unauthorized send; another produces a correct draft with permitted reads only. Both may match the final-text label, but the first violates the action policy and must fail the safety dimension.

## Guided practice

1. Extend the question set into agent scenarios with outcome and action constraints.
2. Store actual calls, observations, final status, committed effects and resource use.
3. Evaluate the simple workflow, single agent and specialist version on the same scenarios.
4. Add repeated trials without presenting them as additional independent cases.
5. Inspect failures by first broken boundary and write a release recommendation with limitations and a proposed real-world pilot metric.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Differentiate outcome evaluation, trajectory constraints and exact transcript matching. Explain judge validation, paired comparisons, experimental units, effect sizes and guardrails. Tie quality improvements to a measurable user task instead of a generic agent score.

## Knowledge check

1. Why not require one exact trajectory?
2. Should an attempted forbidden action be recorded?
3. Are ten repeats ten independent scenarios?
4. Does significance prove business value?

### Answer key

1. Several valid paths may satisfy the same constraints.
2. Yes, separately from whether the tool gateway executed it.
3. No; report case diversity and repeated trials separately.
4. No; assess effect size, costs and operational relevance.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 19: Agent safety and guardrails](/weeks/week-19/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [LangSmith evaluation concepts](https://docs.langchain.com/langsmith/evaluation)
- [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)
