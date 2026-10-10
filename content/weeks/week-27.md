---
layout: week
week: 27
permalink: /weeks/week-27/
title: Fine-tuning and LoRA
description: Your base model understands general language but repeatedly mishandles
  a domain-specific output pattern.
summary: Your base model understands general language but repeatedly mishandles a
  domain-specific output pattern.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 27
kicker_secondary: Optional · 8 hours
---

## Start with the problem

Your base model understands general language but repeatedly mishandles a domain-specific output pattern. First establish what prompting and retrieval can do. Fine-tuning is an experiment on behavior; it is not a reliable replacement for retrieving fresh business facts.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Choose the adaptation objective

**Think about this first.** What behavior should change after training?

Full fine-tuning updates base parameters. Parameter-efficient approaches train a smaller set of additional or selected parameters. Continued pretraining adapts a language-model objective to domain text; supervised fine-tuning trains on desired task responses. Specify which one your data actually supports.

Compare against a prompted base model using the same evaluation cases. For changing factual knowledge, also consider retrieval with current evidence. If the model fails because a source is missing, training may not address the operational failure. Define success before choosing an adaptation method.

## 2. Understand the low-rank update

**Think about this first.** Which values are trainable in LoRA?

LoRA freezes a base weight matrix and learns a low-rank update, commonly written as W plus a scaled product BA. The matrices A and B are trainable adapters. Rank controls the dimensionality of the update; alpha/scaling and target modules affect its behavior. More rank is not automatically better for a small dataset.

QLoRA combines low-rank adaptation with a quantized base under a specific training setup. It reduces some memory costs but does not remove activations, optimizer state, temporary buffers or sequence-length pressure. Validate support for the actual model, dtype, hardware and library versions.

## 3. Check training and artifact behavior

**Think about this first.** Does a small loss prove the adapter is useful?

No. Watch held-out task quality, overfitting, format errors and regressions on general behavior. Keep split families separate and record learning rate, schedule, sequence length, masks and trainable parameter count. Detect non-finite updates and verify that frozen parameters remain unchanged.

An adapter artifact depends on its base revision, tokenizer and configuration. Save those bindings. If merging adapters for inference, compare merged and unmerged output within the declared numerical tolerance. An inference artifact is not necessarily a resumable training checkpoint.

## Walk through one case

Train an adapter to extract a supplier status into a fixed schema. Compare prompted base and adapted model on unchanged held-out sources. A format improvement from 8/10 to 10/10 does not establish factual improvement if correct labels fall. Report both dimensions and keep the adaptation rejected if it harms the required task.

## Guided practice

1. Write the target behavior and establish prompted-base and simple-rule baselines.
2. Select a small licensed model/data setup within the available memory budget.
3. Configure LoRA targets, rank/scaling and training settings; record actual trainable parameters.
4. Test frozen weights, finite gradients and held-out behavior during the run.
5. Save/reload the adapter with base/tokenizer bindings and compare inference parity. Treat GPU/QLoRA support as an environment-specific extension until executed.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Distinguish LoRA, QLoRA, full tuning, prompt/prefix methods and continued pretraining. Explain catastrophic forgetting, bias/variance and why task/data quality can matter more than adapter size. Discuss adaptation only after you can identify the baseline failure it is meant to improve.

## Knowledge check

1. What is frozen in ordinary LoRA?
2. Does QLoRA make all memory negligible?
3. Why bind an adapter to a base revision?
4. Can format improve while usefulness falls?

### Answer key

1. The base parameters for the targeted adaptation; low-rank adapters are trained.
2. No; activations, optimizer/workspace and other runtime costs remain.
3. Its parameters and interpretation depend on the exact underlying model/configuration.
4. Yes; score factual task correctness separately.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 28: Instruction tuning](/weeks/week-28/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [LoRA paper](https://arxiv.org/abs/2106.09685)
- [PEFT LoRA guide](https://huggingface.co/docs/peft/developer_guides/lora)
