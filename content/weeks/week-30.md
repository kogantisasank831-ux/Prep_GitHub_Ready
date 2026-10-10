---
layout: week
week: 30
permalink: /weeks/week-30/
title: Serving and documentation
description: A saved model is not yet a usable service.
summary: A saved model is not yet a usable service.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 30
kicker_secondary: Optional · 8 hours
---

## Start with the problem

A saved model is not yet a usable service. Serving binds weights, tokenizer, template, limits and runtime behavior into a reproducible interface. Finish the course with a measured experiment report that distinguishes useful answer quality from successful transport.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Package what inference actually needs

**Think about this first.** What happens if the tokenizer changes after training?

The same text can produce different token IDs or special-token boundaries, changing behavior even when weights are unchanged. Bind base/adapter revisions, tokenizer, template, generation settings and task schema in a manifest. Verify artifact hashes and reload behavior before starting the service.

Keep inference artifacts separate from resumable training checkpoints. Document the accepted input contract, maximum context/output, deterministic validation and error behavior. A custom HTTP endpoint is not OpenAI-compatible merely because it returns generated text; compatibility requires the actual request/response and streaming contract.

## 2. Measure memory and scheduling

**Think about this first.** Why can a model load but fail under concurrent requests?

Weights are only part of runtime memory. KV cache grows with active cached tokens; activations, buffers and allocator overhead need room too. Quantization changes selected representations and may affect quality, supported kernels and speed. Measure on the actual hardware/runtime rather than assuming lower precision is always faster.

Prefill processes input context; decode generates successive tokens. Continuous batching can improve utilization as requests arrive and finish. Admission limits, context caps and cancellation control resource pressure. Streaming, prefix caching, paged KV management and attention kernels solve different parts of the serving problem.

## 3. Report results that someone else can reproduce

**Think about this first.** Does twelve successful HTTP responses make a model release-ready?

It proves those requests completed under that setup, not that the answers are useful or capacity is sufficient. Report actual workload, concurrency, input/output distributions, successes/errors, client latency and resource usage. Distinguish internal first-token timing from a token actually received by a streaming client.

The experiment report should include objective, permitted data, splits, training configuration, artifacts, compute, loss curves, evaluation, failures, costs and baseline comparison. Retain a clear release decision and limitations. A weak tiny model is an acceptable learning result when the evidence is honest and the pipeline is understood.

## Walk through one case

Load a checksummed bundle, run the same fixed requests at concurrency one and then a small higher level, and compare results and latency. If admission rejects excess requests predictably, record those rejections rather than excluding them. If the tuned model formats answers correctly but misclassifies status, keep it rejected for task use even though serving works.

## Guided practice

1. Create a versioned inference manifest and verify reload/output consistency.
2. Expose a bounded local service with validation, admission limits and explicit error responses.
3. Measure a small fixed workload and distinguish cold/warm and client/server timings.
4. Compare task quality with the previous week's baselines under the served configuration.
5. Publish an experiment report with actual artifacts, resource assumptions, failures and a release decision. Distributed serving, GPU quantization and engine-specific extensions require their own executed evidence.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Compare vLLM, llama.cpp and other runtimes through hardware, model support, concurrency and operational requirements rather than universal rankings. Explain tensor parallelism versus data parallelism, inference versus distributed training, and why GQA architecture differs from a runtime setting. State which features you actually exercised.

## Knowledge check

1. What must an inference bundle bind?
2. Why leave memory headroom?
3. Is internal first-token time streaming TTFT?
4. What determines release readiness?

### Answer key

1. Model/adapter, tokenizer, template, generation settings and task/configuration identities.
2. KV, activations, buffers and runtime overhead grow beyond model weights.
3. No; client-observed streaming time includes the delivery path.
4. Required quality, policy, reliability and resource evidence, not transport success alone.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Return to the [roadmap](/#roadmap), identify the weakest interview or implementation area, and repeat its exercise with a new case. The core 24-week track and optional training experiment should now support a coherent, evidence-backed project story.

## Primary sources

- [vLLM serving documentation](https://docs.vllm.ai/en/latest/serving/openai_compatible_server/)
- [llama.cpp project](https://github.com/ggml-org/llama.cpp)
