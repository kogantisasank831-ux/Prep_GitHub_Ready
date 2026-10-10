---
layout: week
week: 14
permalink: /weeks/week-14/
title: Workflows versus agents
description: 'You can predict the investigation steps: load the invoice, look up the
  contract, compare values and draft a finding.'
summary: 'You can predict the investigation steps: load the invoice, look up the contract,
  compare values and draft a finding.'
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 14
kicker_secondary: 8 hours
---

## Start with the problem

You can predict the investigation steps: load the invoice, look up the contract, compare values and draft a finding. A workflow is a strong starting point. Add model-directed planning only where the next useful action genuinely depends on uncertain observations.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Choose control flow before choosing a framework

**Think about this first.** Which decisions require language-model judgment?

A workflow follows known transitions. An agent chooses actions based on its current state and observations. Both can call models and tools; using an LLM inside a fixed pipeline does not automatically make the pipeline an autonomous agent.

List the decisions in your task. Deterministic validation, access checks and arithmetic should remain code. Ambiguous user intent or selecting an evidence route may benefit from a model. Start with a workflow baseline and measure where it fails before adding an agent loop.

## 2. Compose small, inspectable steps

**Think about this first.** What is the advantage of a chain over one giant prompt?

Each step has a contract and a failure you can locate. A sequence handles dependent operations; routing selects an appropriate branch; parallel execution handles independent work. Preserve intermediate observations so a final answer can be traced to actual evidence.

LangChain offers model/tool interfaces and composition patterns. LangGraph makes state and transitions explicit. Neither removes the need for contracts or evaluation. Keep business logic independent of the framework so a routing policy or storage adapter can be tested without running a full model loop.

## 3. Make the agent alternative earn its extra work

**Think about this first.** Would more steps necessarily improve the answer?

Additional calls can create extra latency, cost and failure opportunities. Bound the plan horizon, available tools, loop count and evidence size. Define a stopping condition, including unresolved and escalated outcomes. A “keep trying until correct” instruction is not an execution budget.

Compare workflow and agent on the same cases. Record correctness, unsupported actions, number of calls and elapsed time. Include an ambiguous case where adaptation helps and a straightforward case where planning adds no value. The objective is useful task completion under constraints, not maximizing autonomy.

## Walk through one case

For a missing contract number, a fixed workflow may stop after direct lookup. An agent may search supplier aliases and locate a linked contract, provided each route is authorized and bounded. If the number is already present, the workflow should complete directly. Comparing those two cases helps distinguish useful adaptation from unnecessary planning.

## Guided practice

1. Write the deterministic investigation as a sequence of typed steps.
2. Add one model decision at an explicitly ambiguous boundary, keeping the tool gateway unchanged.
3. Specify step, time and result-size budgets and a final outcome schema.
4. Run both versions on fixed straightforward, ambiguous and missing-evidence cases.
5. Explain each extra call in the adaptive version and remove calls that do not address an observed failure.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Recognize routing, parallelization, orchestrator-worker and evaluator-reviser patterns, but choose by dependency and failure mode. An evaluator loop needs independent evidence and a limit; two models agreeing does not establish correctness. LangChain composition and LangGraph state are implementation choices after the control-flow decision.

## Knowledge check

1. Can a workflow contain an LLM?
2. What should remain deterministic?
3. What is a meaningful baseline?
4. When should an agent stop?

### Answer key

1. Yes; the distinction is who controls transitions.
2. Authorization, invariants, arithmetic and execution budgets.
3. The simplest fixed workflow that can satisfy the same task.
4. On success, bounded failure, missing evidence, escalation or exhausted budget under an explicit policy.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 15: LangGraph fundamentals](/weeks/week-15/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
- [LangChain overview](https://docs.langchain.com/oss/python/langchain/overview)
