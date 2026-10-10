---
layout: week
week: 20
permalink: /weeks/week-20/
title: Reliability and failure handling
description: A timeout tells you that the caller did not receive a result in time.
summary: A timeout tells you that the caller did not receive a result in time.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 20
kicker_secondary: 8 hours
---

## Start with the problem

A timeout tells you that the caller did not receive a result in time. It does not tell you whether the remote operation executed. Reliable systems distinguish uncertain outcomes from known failures and make repeated work safe.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Classify errors before retrying

**Think about this first.** Should malformed input be retried five times?

No. Validation and authorization errors normally require a changed request or policy decision. Transient network failures may merit bounded retry. A write with an uncertain outcome requires reconciliation by idempotency key before another effect is attempted.

Use exponential backoff with jitter, a maximum attempt count and an overall deadline. Retries consume the same latency and resource budget as the original work. A timeout wrapper that abandons waiting may leave the underlying task running. Cancellation and resource cleanup need to be tested explicitly.

## 2. Bound concurrency and queue work

**Think about this first.** Does async automatically limit outgoing model calls?

No. Awaiting suspends a coroutine while it waits; it does not impose a concurrency or rate limit. Use semaphores for active work, rate/token budgets for provider limits and bounded queues for backlog. A queue without a size limit can turn overload into memory exhaustion.

Durable workers need claim/lease behavior, attempt counts, retry scheduling and dead-letter handling. A crashed worker may leave a job available for redelivery, so effects must be idempotent. Persist enough state to reconcile the result and distinguish a lost response from a failed operation.

## 3. Design degraded behavior and recovery

**Think about this first.** What should happen when the dependency stays unavailable?

A circuit breaker can stop repeated calls after a defined failure condition and allow controlled probes later. A fallback should state reduced capability and preserve the same access/policy boundary. Stale cached data needs a visible freshness policy.

Test recovery after an outage, not just initial rejection. Include shutdown while work is active and restart with queued jobs. Measure queue age, retries, deadline exhaustion, dependency errors and outcome duplication. Availability is not useful if successful responses violate business constraints.

## Walk through one case

A worker sends create-draft with key K, the service commits it, and the response is lost. After retry, the service finds K and returns the original draft ID. Without K, a second draft could appear. If K is reused with different content, reject the mismatch rather than treating it as the same request.

## Guided practice

1. Classify validation, policy, transient and uncertain-write failures.
2. Add bounded retries, jitter, a total deadline and an injectable clock for tests.
3. Protect active work with a concurrency limit and queue backlog with a size limit.
4. Implement durable job state and idempotent effect reconciliation.
5. Inject lost responses, worker crashes, repeated delivery, dependency outage and shutdown. Verify one logical effect and eventual visible outcome.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Explain concurrency versus parallelism, semaphore versus rate limiter, and retry versus recovery. At-least-once delivery is compatible with one logical business effect only when application idempotency and transactional boundaries support it. Avoid claiming exactly-once execution merely because the queue acknowledges messages.

## Knowledge check

1. What does await limit?
2. Does timeout mean no effect occurred?
3. Why jitter backoff?
4. What happens when an idempotency key has different content?

### Answer key

1. Nothing by itself; it yields while waiting.
2. No; reconcile uncertain writes.
3. To reduce synchronized retry bursts across callers.
4. Reject the conflict rather than duplicate or overwrite the original effect.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 21: Cost and latency optimisation](/weeks/week-21/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [Python asyncio synchronization](https://docs.python.org/3/library/asyncio-sync.html)
- [Amazon retry/backoff guidance](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)
