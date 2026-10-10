---
layout: week
week: 15
permalink: /weeks/week-15/
title: LangGraph fundamentals
description: An investigation fails after retrieving a contract.
summary: An investigation fails after retrieving a contract.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 15
kicker_secondary: 8 hours
---

## Start with the problem

An investigation fails after retrieving a contract. You want to resume without losing the evidence or creating a duplicate action. An explicit state graph makes the next step and saved progress inspectable, but persistence alone does not guarantee exactly-once side effects.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Define state before drawing nodes

**Think about this first.** What information must survive a pause?

State should contain the task identity, trusted scope reference, observations, decision status and pending action metadata. Keep values serializable and bounded. Avoid storing arbitrary runtime objects or unrestricted conversation history in the checkpoint.

A node reads state and returns a state update. Edges define transitions; conditional edges use validated outcomes. A reducer determines how concurrent updates combine. Appending messages, replacing a field and merging keyed observations have different semantics. A careless reducer can duplicate stale observations after retries.

## 2. Treat persistence as a consistency problem

**Think about this first.** Does a checkpointer make an external write exactly once?

No. Saving graph state and committing a tool effect are distinct operations. A crash can occur between them. Use idempotent effect boundaries and reconcile outcome by operation ID. Bind each thread or run to an authorized owner; possession of a thread ID is not permission to read or resume it.

LangGraph checkpointers enable persisted state and resumption under their configured execution model. Understand which node can replay after failure or interruption. Keep nondeterministic work and effects in appropriate durable boundaries, and test the behavior of the exact framework version you install.

## 3. Design interruption and streaming deliberately

**Think about this first.** What is the user approving during a paused run?

They should see the exact pending action, scope and evidence, not an ambiguous “continue” button. Persist a digest or immutable action version, expiry and authorized reviewer. After resumption, verify approval still matches the action and current policy.

Streaming state updates and streaming model tokens are different interfaces. Expose bounded, user-appropriate progress; avoid leaking internal prompts or private tool results. Subgraphs can encapsulate a reusable workflow but need explicit input/output and persistence ownership. Test cancellation and interrupted work separately from ordinary completion.

## Walk through one case

Pause before creating a supplier-review draft. Save the proposed draft and its digest. While waiting, a new contract revision appears. On resume, do not silently execute a changed draft under old approval. Either validate that the original action is still permitted or create a new proposal for review. The checkpoint stores continuity; the approval service enforces permission.

## Guided practice

1. Define a typed state and implement retrieve, compare, propose and finish nodes.
2. Add conditional edges for insufficient evidence and failure, plus an explicit terminal state.
3. Use a persistent checkpointer and verify resume in a new process.
4. Interrupt before a write and bind approval to the proposed action/version.
5. Test replay, duplicate resume, cross-owner thread access and stale approval. Record the actual persistence backend and framework version used.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Explain state, node updates, edges, reducers and checkpoints with one failure timeline. Separate checkpoint recovery from idempotent tool execution. Discuss streamed events, subgraph contracts and ownership of a long-running thread. A diagram is useful only if you can say which data is durable at each transition.

## Knowledge check

1. What does a reducer control?
2. Is a thread ID an authorization token?
3. Why can a resumed write duplicate?
4. What makes approval stale?

### Answer key

1. How multiple updates to a state field combine.
2. No; the application must verify ownership and scope.
3. The effect and checkpoint may commit separately; replay needs idempotency.
4. A changed action, scope, evidence version, expiry or policy can invalidate it.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 16: Memory and context engineering](/weeks/week-16/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
