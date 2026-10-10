---
layout: week
week: 13
permalink: /weeks/week-13/
title: Tool calling
description: A model can suggest “look up this supplier,” but your application must
  decide whether that lookup exists, which arguments are valid and who may execute
  it.
summary: A model can suggest “look up this supplier,” but your application must decide
  whether that lookup exists, which arguments are valid and who may execute it.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 13
kicker_secondary: 8 hours
---

## Start with the problem

A model can suggest “look up this supplier,” but your application must decide whether that lookup exists, which arguments are valid and who may execute it. Tool calling is a request protocol. The model's proposed action becomes real only after a trusted executor accepts it.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Make the tool contract narrow

**Think about this first.** What would an unrestricted execute_sql tool allow?

It delegates too much authority and makes authorization hard to reason about. Prefer domain operations such as lookup_supplier or compare_invoice_price with bounded fields and stable result schemas. Resolve identity from the application session, never from model-supplied arguments.

The tool description helps the model choose correctly; the schema constrains structure. Validate enum values, identifiers, number bounds and unknown fields. Then authorize the specific operation. Use parameterized database access behind the tool, with scope predicates enforced in the query layer.

## 2. Separate proposals, observations and decisions

**Think about this first.** Does a tool-call-shaped JSON object prove that a tool ran?

No. Distinguish proposed calls from accepted calls and returned observations. Keep call IDs, tool revision, validated arguments, status and bounded results. Feed observations back as data with provenance. A model must not claim a successful write because it merely generated a call.

Read-only operations can often be retried safely; writes need idempotency and approval rules. A timeout does not prove a write failed. Use a stable idempotency key to inspect or resume the original effect instead of creating another order or draft.

## 3. Bound the execution loop

**Think about this first.** How does the agent stop when the same lookup keeps failing?

Set limits on steps, repeated calls, tool duration, response bytes and total cost. Classify errors so invalid arguments are repaired differently from transient transport failures. A fallback must remain within the same authorization boundary.

Parallelize independent reads only. If comparing an invoice requires a supplier ID found in a prior lookup, that dependency must complete first. Concurrency is not a substitute for a correct dependency graph. Keep the final answer tied to actual observations and disclose missing evidence.

## Walk through one case

The user asks whether invoice I-42 exceeds the contracted unit price. First resolve the authorized invoice, then its supplier and contract revision, then compare compatible currency/unit values. The model can organize the request, but deterministic code performs decimal arithmetic and checks units. The answer cites the actual observations; a missing contract produces an unresolved result.

## Guided practice

1. Implement two read-only tools with strict input/output schemas and explicit authorization.
2. Write a dispatcher that rejects unknown tool names, extra fields and unauthorized identifiers.
3. Add bounded results and a stable error taxonomy. Keep payloads out of general logs.
4. Exercise a dependent lookup chain and two independent reads.
5. Test invalid arguments, duplicate requests, timeout uncertainty and fabricated model claims. The existing document service provides a typed-boundary example to extend.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Explain tool choice separately from execution authority. Framework bindings can simplify schema transport, but permissions, SQL safety, monetary calculations, idempotency and approvals belong in deterministic services. Describe when a direct function call is simpler than a model-selected tool.

## Knowledge check

1. Who establishes identity?
2. Is a call proposal an observation?
3. Can dependent lookups run together?
4. Why are write retries dangerous?

### Answer key

1. The trusted application/session, not tool arguments.
2. No; only the executor can return a verified execution result.
3. Only once their required inputs are available.
4. The first effect may have succeeded despite a timeout; use idempotency and status reconciliation.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 14: Workflows versus agents](/weeks/week-14/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [Pydantic strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [Python decimal arithmetic](https://docs.python.org/3/library/decimal.html)
