---
layout: week
week: 16
permalink: /weeks/week-16/
title: Memory and context engineering
description: A user says “use the same supplier as before.
summary: A user says “use the same supplier as before.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 16
kicker_secondary: 8 hours
---

## Start with the problem

A user says “use the same supplier as before.” Keeping the entire conversation forever is expensive and can preserve stale or malicious instructions. Memory should retain the facts needed for the task, their source and their lifetime.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Separate working context from durable memory

**Think about this first.** Does every previous message belong in the next prompt?

No. Working context holds the current task, relevant observations, pending decisions and recent messages. Durable memory stores selected facts or preferences across tasks. A checkpointer saves execution state; it is not automatically a curated long-term memory system.

Define what is eligible for storage. A verified supplier ID, a user-confirmed preference and an untrusted model inference deserve different treatment. Attach source, owner, timestamp, version and confidence or verification status where meaningful. Keep instructions found in documents from becoming trusted policy through a summary.

## 2. Compact without losing the task

**Think about this first.** What must survive when a long conversation is summarized?

Preserve the current objective, constraints, decisions, source references, pending actions and unresolved questions. Retain exact identifiers and numerical conditions. A summary that drops “do not send” can change the allowed action. Keep a route to the original evidence and test summaries against concrete invariants.

Use a context budget: reserve system rules, current request, tool schemas and output, then select history/evidence. Rolling windows are simple but can discard old commitments. Structured summaries reduce repetition but can introduce errors. Retrieval of older messages can help when source and owner filters remain intact.

## 3. Make memory editable and forgettable

**Think about this first.** How do you stop an old preference from overriding a new one?

Version memory entries and distinguish explicit user corrections from inferred preferences. Support expiry, correction and deletion under an owner boundary. A deleted entry must also be removed or invalidated in derived indexes and caches according to the retention design.

Evaluate memory through behavior: correct follow-up resolution, resistance to cross-user leakage, preservation of constraints and recovery from stale information. “The summary is shorter” is not enough. Compare task success and token use using the same conversation scenarios.

## Walk through one case

The user first says “draft a supplier email, do not send,” then asks for several revisions. A compacted context must preserve the prohibition and the draft identity. Later “looks good” does not automatically authorize sending. An explicit send request should create a separately authorized action under the tool policy, with the final draft version bound to it.

## Guided practice

1. Define a structured summary with objective, constraints, decisions, evidence and pending work.
2. Add bounded recent turns and retrieve older evidence only when needed.
3. Store long-term entries by trusted owner with source, revision and expiry.
4. Test follow-up resolution, changed preferences, deletion and malicious stored text.
5. Compare full-history, rolling-window and structured-summary strategies on fixed tasks. Record what each loses and which tasks get worse.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Explain short-term state, long-term memory and retrieval as separate mechanisms. Semantic, episodic and procedural memory labels are useful only when they map to actual data and update policies. Memory retrieval requires the same access discipline as document retrieval. Token savings are valuable when task constraints survive.

## Knowledge check

1. Is a checkpoint curated memory?
2. What must compaction preserve?
3. How should corrections work?
4. What proves a memory design helps?

### Answer key

1. No; it saves execution state and may contain stale or excessive material.
2. Goals, constraints, exact facts/IDs, decisions, pending actions and evidence pointers.
3. Version or supersede entries with provenance and invalidate derived stale copies.
4. Behavioral evaluation across continuity, leakage, stale data and resource use.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 17: Multi-agent systems](/weeks/week-17/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [LangGraph memory](https://docs.langchain.com/oss/python/langgraph/memory)
- [Context engineering](https://docs.langchain.com/oss/python/langchain/context-engineering)
