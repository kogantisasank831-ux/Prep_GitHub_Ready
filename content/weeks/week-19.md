---
layout: week
week: 19
permalink: /weeks/week-19/
title: Agent safety and guardrails
description: An investigation ends with “create a supplier-review draft.
summary: An investigation ends with “create a supplier-review draft.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 19
kicker_secondary: 8 hours
---

## Start with the problem

An investigation ends with “create a supplier-review draft.” The model may propose that action, but approval must refer to exactly what will happen. Safety becomes concrete when you can identify the action, reviewer, expiry and resulting effect.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Place policy at the effect boundary

**Think about this first.** Can an approval prompt enforce a spending limit?

It can explain a rule, but deterministic code must enforce it. Separate content checks, task validation, authorization and business policy. Guardrails frameworks can organize these checks; their classifiers and model-based judges remain fallible.

Define tool scopes and an allowlist of effects. A draft operation should create a draft, not send a message under a similarly named tool. Keep high-impact actions separate from read-only investigation. The final executor rechecks policy regardless of which agent proposed the action.

## 2. Bind approval to an immutable proposal

**Think about this first.** What does “approved” refer to after the draft changes?

It must refer to a specific proposal/version or digest, trusted reviewer, scope and expiry. Store pending, approved, rejected, expired and executed states with clear transitions. An altered proposal needs a new decision. A string saying “approved” inside model output is not a reviewer decision.

Handle races transactionally. Two concurrent resume requests must not produce two effects. Reserve a stable idempotency key and store the effect outcome. Recheck current permissions and relevant source freshness immediately before execution. A once-valid approval may no longer permit the action.

## 3. Audit decisions without exposing payloads

**Think about this first.** What should an audit record let you reconstruct?

Record who proposed, reviewed and executed which action, under what policy/version, with timestamps and evidence references. Use bounded identifiers and protected payload references rather than unrestricted source text in general logs. A reliable audit trail supports both debugging and user-visible explanations.

Test the bypass paths: direct tool access, replayed decisions, another reviewer, expired approval and changed action content. Defense in depth includes validators, scoped tools and review, but the final business invariant should remain enforced even if the model or detector fails.

## Walk through one case

A reviewer approves draft D version 2. Before execution, the agent updates its recipient, producing version 3. Reusing the version-2 approval would authorize a different action. Reject that attempt, create a new pending decision, and keep the original audit history. Duplicate execution requests for the approved version should return the stored outcome.

## Guided practice

1. Define proposal and approval records with trusted actor, action digest and expiry.
2. Implement deterministic state transitions and enforce them at the tool boundary.
3. Add idempotent execution and a durable outcome record.
4. Test stale, forged, cross-owner and duplicate approvals, including concurrent calls.
5. Write a user-facing explanation for rejected or expired actions and a minimal audit view.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Contrast input filtering, output validation, policy checks and human approval. Explain why NeMo Guardrails or another orchestration layer complements authorization instead of replacing it. Discuss the exact moment an external effect becomes possible and how retries are reconciled.

## Knowledge check

1. Who can approve an action?
2. What invalidates a previous approval?
3. Why use an idempotency key?
4. Where must policy run?

### Answer key

1. An authenticated, authorized reviewer under the business policy.
2. Changed action/version/scope, expiry or current policy restrictions.
3. To reconcile repeats to the same effect rather than execute again.
4. At the actual effect boundary, including direct and replayed calls.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 20: Reliability and failure handling](/weeks/week-20/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [NeMo Guardrails documentation](https://docs.nvidia.com/nemo/guardrails/latest/index.html)
