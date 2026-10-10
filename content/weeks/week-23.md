---
layout: week
week: 23
permalink: /weeks/week-23/
title: GenAI system design
description: An interviewer asks you to design an enterprise assistant.
summary: An interviewer asks you to design an enterprise assistant.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 23
kicker_secondary: 8 hours
---

## Start with the problem

An interviewer asks you to design an enterprise assistant. Starting with a vector database and a model name skips the decisions that determine whether the system is useful. Begin with users, tasks, constraints and measurable failure costs, then draw only the components those requirements justify.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Turn requirements into a task contract

**Think about this first.** Who uses the assistant and what may it do?

Clarify document types, source freshness, languages, identity model, read/write actions and human escalation. Distinguish a search assistant from an agent that changes business state. Identify unacceptable failures, such as cross-tenant disclosure or an unsupported approval.

Define quality and service metrics: evidence-supported task success, abstention, action-policy violations, client latency and availability. Ask for workload information rather than assuming every registered user sends concurrent requests. Use ranges when traffic or document sizes are uncertain and identify what needs measurement.

## 2. Follow data and authority through the architecture

**Think about this first.** Where does a document become visible to a query?

Describe ingestion, validation, parsing/chunking, metadata and index publication. Then follow authentication, authorized retrieval, reranking, context, generation, validation and display. Explain the version boundary linking an answer to its sources. Add tools only for tasks that need external operations.

Place deterministic controls at actual resource/effect boundaries. Show how queues, caches and checkpoints preserve scope. Discuss deletion and permission changes through derived indexes and caches. Choose the simplest storage and serving arrangement that meets measured requirements before adding multi-agent or distributed complexity.

## 3. Defend capacity, evaluation and failure behavior

**Think about this first.** What happens when the model is slow or the index is unavailable?

Estimate active request concurrency from arrival rate and time in the system under stated assumptions. Separate prefill/decode and non-model stages. Budget memory beyond weights, and validate estimates with representative load. State which latency/capacity numbers are estimates.

Define offline cases, rollout gates, monitoring and rollback before claiming readiness. Handle missing evidence, dependency failure, overload and uncertain writes explicitly. A graceful fallback must preserve authorization and disclose reduced capability. Balance freshness, quality, latency and cost with evidence rather than a universal architecture.

## Walk through one case

For a procurement copilot, choose read-only cited answers first and approval-bound drafts second. Ingestion publishes complete corpus revisions. Queries use authenticated scope and source-versioned citations. A draft is a separately validated proposal, with human approval before any permitted effect. This architecture supports an incremental launch and creates clear evaluation boundaries.

## Guided practice

1. Design an enterprise RAG platform and a customer-support agent as two separate exercises.
2. Write assumptions, success metrics and prohibited outcomes before drawing components.
3. Trace one successful request, one denied request and one dependency failure.
4. Include rough workload/memory calculations with stated assumptions and validation plans.
5. Record a ten-minute explanation and revise any component whose responsibility or failure behavior you cannot explain.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Use requirements → metrics → data → architecture → retrieval/tools → model choice → evaluation → deployment → monitoring → security → cost → recovery. Adapt to an analytics assistant, research agent or multi-tenant document service by changing task/data constraints, not by reciting the same component diagram.

## Knowledge check

1. What comes before model selection?
2. Why distinguish search from action?
3. How should unknown capacity be presented?
4. What makes a component justified?

### Answer key

1. Task, users, constraints, failure costs and measurable requirements.
2. Changing state requires stronger policy, approval and idempotency boundaries.
3. As an assumption/range plus a concrete measurement plan.
4. A specific requirement or measured bottleneck it addresses.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 24: Project storytelling and mock interviews](/weeks/week-24/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [Google SRE monitoring guidance](https://sre.google/sre-book/monitoring-distributed-systems/)
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
