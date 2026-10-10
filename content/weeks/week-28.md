---
layout: week
week: 28
permalink: /weeks/week-28/
title: Instruction tuning
description: An instruction dataset teaches a model how to respond to a request, including
  when to say the evidence is insufficient.
summary: An instruction dataset teaches a model how to respond to a request, including
  when to say the evidence is insufficient.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 28
kicker_secondary: Optional · 8 hours
---

## Start with the problem

An instruction dataset teaches a model how to respond to a request, including when to say the evidence is insufficient. The chat template and loss mask define the task as much as the visible text. Inspect the actual tokens before starting training.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Build examples that represent decisions

**Think about this first.** Would repeating one successful answer create a useful instruction model?

It can teach a narrow pattern while leaving the real decision boundary untouched. Include varied instructions, correct outputs, absent evidence, conflicting facts and format constraints. Keep labels tied to authorized evidence. Avoid treating a synthetic model answer as verified truth without checking it.

Separate scenario families across splits. Include instruction paraphrases within the same family and keep the final test untouched. Document dataset construction and review so improvements can be attributed to a reproducible change rather than a quietly altered reference set.

## 2. Inspect the template and loss mask

**Think about this first.** Which tokens should the model learn to emit?

Serialize messages with the target model's chat template and special-token policy. Avoid adding BOS/EOS twice or using one template for training and another at inference. Verify prompt, assistant response and end-of-turn boundaries on actual token IDs.

Assistant-only loss masks exclude prompt tokens from the supervised objective, while other objectives intentionally include more text. State the policy and inspect padding/truncation behavior. If truncation removes the answer or its terminating token, the record no longer teaches the intended task. Empty-target records should be handled explicitly.

## 3. Compare behavior after a small controlled run

**Think about this first.** Does the model obey instructions outside the training phrasing?

Evaluate unseen source families, alternative wording and insufficient-evidence cases. Compare to prompted base under the same template. Track schema validity, required claims, unsupported facts and abstention. Monitor general-task regressions when specialization may displace useful behavior.

SFT learns from desired responses. Preference optimization learns from relative preferences under its chosen objective; reinforcement learning uses a reward-driven policy update; distillation transfers behavior or distributions from a teacher. These are different data and optimization setups, not interchangeable names for the same training command.

## Walk through one case

A record asks for an approval date but the source contains only “approval pending.” The correct response reports the date as unknown. If every training answer contains a date, the dataset teaches pressure to invent one. Add reviewed insufficient-evidence examples and inspect whether the model preserves the unknown case on a new supplier family.

## Guided practice

1. Author a small instruction set with task diversity and evidence-backed expected responses.
2. Serialize with one pinned template and inspect input/target/mask triples.
3. Reject examples whose target disappears after truncation or whose reference contradicts the source.
4. Run a small SFT experiment and compare prompted-base versus tuned behavior.
5. Save data/template/model bindings and report format, correctness and abstention separately. Keep preference/RL/distillation extensions out of the result unless actually run.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Explain what the template tells the model, what the mask tells the optimizer and how train-serve skew can appear. Distinguish desired-answer examples from preference pairs and rewards. Discuss instruction diversity and overfitting using concrete held-out failures.

## Knowledge check

1. Why inspect token IDs?
2. What does assistant-only masking exclude?
3. Why include unknown answers?
4. Is SFT the same as RL?

### Answer key

1. Visible text can hide duplicated special tokens, wrong boundaries or missing targets.
2. Prompt and other non-target positions under the declared policy.
3. To teach correct insufficiency when evidence does not supply the requested fact.
4. No; objectives, supervision and optimization differ.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 29: Model evaluation](/weeks/week-29/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [Chat templates](https://huggingface.co/docs/transformers/chat_templating)
- [TRL SFT trainer](https://huggingface.co/docs/trl/sft_trainer)
