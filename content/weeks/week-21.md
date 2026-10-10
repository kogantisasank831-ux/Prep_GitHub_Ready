---
layout: week
week: 21
permalink: /weeks/week-21/
title: Cost and latency optimisation
description: Before choosing a smaller model, count where the work goes.
summary: Before choosing a smaller model, count where the work goes.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 21
kicker_secondary: 8 hours
---

## Start with the problem

Before choosing a smaller model, count where the work goes. A chat request may spend more time retrieving oversized context or repeating an unchanged prefix than doing useful reasoning. Optimize a measured bottleneck while preserving the task's quality and safety requirements.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Separate costs and latency components

**Think about this first.** Which tokens does a cache actually avoid computing?

Track input, output, repeated prompt prefixes, retrieved evidence and model/tool calls separately. Provider billing and self-hosted compute have different accounting. Prefix/KV reuse can avoid repeated prefill work under a compatible engine and prompt, while response caching skips a larger part of the pipeline. Neither should be described as universally free.

Measure client-visible latency, queue delay, time to first received token and completion time. Streaming improves perceived responsiveness but does not necessarily reduce total compute. Compare p50/p95 under representative input/output lengths and concurrency, with warm and cold behavior distinguished.

## 2. Cache and route under the same policy

**Think about this first.** Can two tenants reuse a cached answer?

Only if the cache policy proves the answer is shareable. Include relevant access scope, source revision, prompt/model identity and normalized request semantics in the key. Time-to-live alone does not handle revoked access. Semantic caches add false-match risk and need task-level validation, especially for numbers and exact identifiers.

Route simple tasks to an appropriate small model or deterministic tool, escalating only when a validated rule indicates the need. Model confidence is not automatically calibrated. Keep unresolved cases and extra escalation calls in the quality/cost report; a cheap first call plus frequent fallback can cost more.

## 3. Budget context and memory deliberately

**Think about this first.** Does fitting model weights guarantee serving capacity?

No. Runtime memory also includes KV cache, activations, temporary buffers and overhead. For a simplified decoder KV estimate, multiply layers, KV heads, head dimension, two K/V tensors, bytes per value and active cached tokens. GQA reduces KV heads relative to query heads; use the actual configuration.

Context pruning and summaries can reduce input work but must preserve constraints and required evidence. Compare quality before and after each change. Throughput improvements from batching can trade against per-request latency. Registered users are not the same quantity as concurrent active sequences.

## Walk through one case

Suppose a request repeatedly includes a long unchanged policy and a small new question. First measure prefill and total latency. Test engine-supported prefix reuse, then test a smaller evidence packet. Keep output quality and permission scope fixed. If the smaller packet drops a contractual exception, reject that optimization despite its token savings.

## Guided practice

1. Instrument stage latency, tokens or clearly labeled estimates, retries and cache behavior.
2. Establish a quality baseline and explicit minimum acceptable outcomes.
3. Compare one change at a time: context pruning, exact cache, conditional routing or prefix reuse.
4. Test tenant separation, changed source versions, exact numbers and low-confidence escalation.
5. Report quality, p50/p95, calls and resource/cost assumptions together. Do not extrapolate a three-request demo into a concurrency guarantee.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Distinguish response caching, embedding caching, prefix/KV caching and model routing. Explain prefill versus decode, GQA versus quantization and active-token capacity. LiteLLM or serving middleware can route and account for requests, but application access, factuality and cache invalidation remain explicit responsibilities.

## Knowledge check

1. Does streaming guarantee lower total latency?
2. Why include scope in a cache key?
3. What is missing from weights-only memory math?
4. How should an optimization be accepted?

### Answer key

1. No; it changes when partial output becomes visible.
2. To avoid reusing evidence or answers across incompatible permissions.
3. KV, activations, workspace and runtime overhead.
4. By a controlled comparison that preserves declared quality/policy requirements.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 22: MCP and interoperable tools](/weeks/week-22/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [vLLM automatic prefix caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/)
- [vLLM optimization](https://docs.vllm.ai/en/latest/configuration/optimization/)
