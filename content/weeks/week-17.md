---
layout: week
week: 17
permalink: /weeks/week-17/
title: Multi-agent systems
description: Three specialist agents inspect the same invoice and agree it should
  be approved.
summary: Three specialist agents inspect the same invoice and agree it should be approved.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 17
kicker_secondary: 8 hours
---

## Start with the problem

Three specialist agents inspect the same invoice and agree it should be approved. That agreement is weak evidence if all three copied the same incorrect clause. Specialization helps when responsibilities, observations and authority are explicit; adding more speakers does not create independent verification.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Give each specialist a bounded responsibility

**Think about this first.** What can a specialist do that the coordinator cannot?

A retrieval specialist can locate permitted source spans, an analysis specialist can compare typed values, and a reviewer can check a proposed claim against evidence. Define inputs, outputs, allowed tools and budgets for each. A role name in a prompt is not a permission boundary.

Use a common tool gateway so every specialist obeys the same identity and authorization rules. Pass bounded artifacts rather than copying every conversation into every prompt. Independent reads can run in parallel; dependent work should wait for the required artifact. Preserve source IDs and versions through handoffs.

## 2. Choose a coordination pattern

**Think about this first.** Who decides when the task is finished?

A supervisor can assign bounded subproblems and reconcile results. A handoff transfers control to another agent under an explicit task contract. A deterministic coordinator may be enough when the order is known. Avoid circular conversations with no termination rule.

Conflicting observations need reconciliation against authoritative evidence, not majority voting. Distinguish uncertainty, missing evidence and actual contradiction. If one specialist says Net 15 and another says Net 30, inspect supplier, revision and effective date before summarizing a consensus.

## 3. Evaluate the extra complexity

**Think about this first.** Does a second agent improve the same task?

Compare one-agent and multi-agent versions using unchanged cases and shared tool contracts. Track correctness, invalid actions, calls, tokens, latency and unresolved outcomes. Include a case where handoff loses an identifier or condition. Specialists can multiply work and correlated mistakes.

Interoperability protocols such as A2A describe communication between agents; MCP describes connections to tools/data. Neither grants business authority or proves agent competence. Authentication, scoped artifacts and final action policy remain application responsibilities regardless of the transport.

## Walk through one case

The evidence specialist returns a contract clause with revision and offsets. The analyst returns a decimal-safe variance calculation with unit/currency checks. The reviewer finds the invoice refers to a different revision and blocks the recommendation. This is useful specialization because the reviewer checks a distinct failure, not merely restating the analyst's answer.

## Guided practice

1. Define three specialist artifact schemas and a coordinator outcome.
2. Give every specialist only the tools it needs through the shared authorization gateway.
3. Preserve source lineage and validate artifacts before handoff.
4. Test disagreement, missing artifacts, failed specialists, duplicate messages and exhausted budgets.
5. Compare against a single-agent baseline and explain whether the extra coordination earns its resource cost.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Explain supervisor versus handoff with concrete ownership of state and termination. Discuss correlated failure and why independent evidence matters more than different role prompts. Describe the permissions that remain unchanged across A2A or MCP boundaries.

## Knowledge check

1. Is a specialist role a security boundary?
2. How should agents resolve conflicting clauses?
3. What is a useful baseline?
4. Does majority agreement prove correctness?

### Answer key

1. No; executable permissions must be enforced.
2. Inspect authoritative source identity, version and applicability.
3. One agent or a deterministic workflow using the same tools and cases.
4. No; agents may share the same mistaken evidence or reasoning.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 18: Agent evaluation](/weeks/week-18/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [LangChain multi-agent patterns](https://docs.langchain.com/oss/python/langchain/multi-agent)
- [A2A documentation](https://a2a-protocol.org/latest/)
