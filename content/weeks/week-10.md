---
layout: week
week: 10
permalink: /weeks/week-10/
title: Observability and tracing
description: “It worked last week” is a debugging starting point, not an explanation.
summary: “It worked last week” is a debugging starting point, not an explanation.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 10
kicker_secondary: 8 hours
---

## Start with the problem

“It worked last week” is a debugging starting point, not an explanation. A trace should let you connect an answer to the sources, prompt version and stage behavior that produced it. Begin with a reproducible question and compare the first changed boundary.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Trace a request across stages

**Think about this first.** What connects a search operation to the answer that used it?

A trace groups related execution. A span describes an operation with timing, status and parent identity. Start a request span, then children for retrieval, reranking, packing, generation and validation. Logs describe events; metrics aggregate populations. Use them together rather than expecting one final log line to explain an entire request.

Carry trace context explicitly across thread, HTTP or message boundaries. A new worker should not silently start an unrelated root. Test parent relationships and context cleanup. A correlation ID is not authenticated user identity and must never determine tenant access.

## 2. Record the versions and resources you actually observed

**Think about this first.** Does a token estimate equal a provider bill?

No. Distinguish tokenizer estimates from provider-reported usage. Keep usage unknown when unavailable, and record retries/cache accounting and the applicable pricing version for any cost estimate. Use a monotonic clock for elapsed durations. Root duration is not the sum of overlapping child durations.

Record prompt, model/adapter, corpus, parser/chunker and retrieval configuration identities. Source metadata matters too: changing a supplier or access label can alter behavior without changing text. Link operational spans to a protected evidence record rather than dumping raw prompts, secrets or documents into an unrestricted trace backend.

## 3. Classify the failure before fixing it

**Think about this first.** Should missing evidence and a broken validator look identical?

An insufficient-evidence outcome can be a valid execution, even though it fails an answerable task. A validator exception is an operational failure. Preserve that distinction in both evaluation and monitoring. Use bounded error codes and attributes, payload limits and a retention policy.

Compare source versions, candidate sets, context omissions and model settings before declaring drift. Data drift concerns input distributions; concept drift concerns the relationship to the target; train-serve skew concerns differing transformations or assumptions. A changed PDF parser can explain a regression without any model drift.

## Walk through one case

Run the same payment question four ways: normal, missing controlling clause, corrupted generated claim and delayed retrieval. The missing-source case should change the corpus/evidence record. The corrupt claim should fail at validation despite adequate context. The delay should change retrieval duration while leaving the supported answer intact. Those observations imply different fixes.

## Guided practice

1. Use the OpenTelemetry SDK with a local exporter and a request span containing stage children.
2. Propagate context into one real worker boundary and verify its parent ID.
3. Allowlist trace fields; inspect exported data for raw document or exception text.
4. Inject the three controlled incidents from the worked case and join each trace to its evaluation row.
5. Write an incident note with symptom, changed stage, evidence, smallest fix and regression check. Document cooperative deadlines honestly: timing a call does not interrupt a hung call.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

OpenTelemetry supplies instrumentation and export interfaces. A hosted dashboard is a separate choice. Evaluate sampling, retention, access, cardinality and evidence access before selecting a vendor. For a “wrong today” interview question, compare a successful and failing case under the same task contract; explain what changed first and what remains uncertain.

## Knowledge check

1. Why explicitly propagate context?
2. Why not sum child latency?
3. Does a green trace prove answer correctness?
4. What if provider usage is absent?

### Answer key

1. A boundary may not inherit the active trace; verify real parent relationships.
2. Nested and parallel operations overlap.
3. No. A flawed source-selection policy can execute without exceptions.
4. Keep it unknown; label any separate estimate and its assumptions.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 11: RAG security](/weeks/week-11/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)
- [Context propagation](https://opentelemetry.io/docs/concepts/context-propagation/)
