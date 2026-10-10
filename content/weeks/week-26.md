---
layout: week
week: 26
permalink: /weeks/week-26/
title: Data preparation
description: Training quality depends on the data you actually feed the model, not
  the number of files collected.
summary: Training quality depends on the data you actually feed the model, not the
  number of files collected.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 26
kicker_secondary: Optional · 8 hours
---

## Start with the problem

Training quality depends on the data you actually feed the model, not the number of files collected. Build an auditable pipeline that can explain where each example came from, why it was retained and which split owns it.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Track provenance and permitted use

**Think about this first.** Does public availability establish training permission?

No. Record the source, license or permission, retrieval date and permitted use before including material. Keep original and cleaned versions linked by identifiers/hashes. Apply privacy review and removal policies appropriate to the dataset; a PII detector is a useful aid, not proof that all sensitive content is gone.

Prefer original synthetic or clearly licensed material for the small exercise. Treat document text as data rather than executable instructions. Keep source payloads out of routine logs and do not publish private documents with a model artifact.

## 2. Deduplicate without hiding the split problem

**Think about this first.** When should duplicate families be assigned to splits?

Before training and final evaluation. Exact normalized hashes catch byte/text duplicates; near-duplicate detection finds related passages that can still leak across splits. Group shared source families together. Choose temporal splits when the application must generalize to future data.

Cleaning should preserve meaningful numbers, units, punctuation and language. Track rejection reasons and counts. Language or quality filters can systematically remove useful minority or domain examples, so inspect samples from each rejected group. A longer document is not automatically higher quality.

## 3. Inspect tokens, masks and packed sequences

**Think about this first.** What happens when unrelated documents share one token pack?

You need an explicit boundary policy, separators and attention/loss rules. Packing can improve utilization but may teach transitions across documents if boundaries are ignored. For a simple experiment, keep documents isolated until the intended objective is clear.

Freeze tokenizer revision, special tokens, maximum length, truncation and loss masks. A dataset manifest should bind source versions, split IDs, transformations and output hashes. Re-running should reproduce the same records under that manifest. Keep an untouched evaluation set outside data-driven tuning choices.

## Walk through one case

Two copied contract templates differ only in supplier name. Randomly splitting them can put near-identical phrasing in training and validation. Group the template family, then assign the family to one split. Inspect whether useful differences such as currency or approval conditions survived cleaning; over-normalization can erase exactly what the task should learn.

## Guided practice

1. Define a source manifest with permission, version, hash and document-family IDs.
2. Implement bounded loading, cleaning and exact deduplication with rejection counts.
3. Add a reviewed near-duplicate/family policy and deterministic split assignment.
4. Tokenize and inspect several complete input/target/mask records by hand.
5. Write exports and a transformation manifest. Test split overlap, malformed text, empty documents and changed tokenizer settings.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Connect training contamination to feature leakage in classical ML. Preprocessing fitted on the entire dataset can leak evaluation information. Explain exact versus near deduplication, dataset mixtures, domain balance and why data quality needs task-specific inspection rather than a universal quality score.

## Knowledge check

1. Is public text automatically reusable?
2. Why group template families?
3. What must cleaning preserve?
4. What belongs in a reproducibility manifest?

### Answer key

1. No; retain a permission/license basis for the intended use.
2. Near-duplicate structure can leak across splits.
3. Facts and distinctions relevant to the task, including numbers and conditions.
4. Source/split identities, transforms, tokenizer, configuration and output hashes.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 27: Fine-tuning and LoRA](/weeks/week-27/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [Hugging Face Datasets processing](https://huggingface.co/docs/datasets/process)
- [Data leakage guidance](https://scikit-learn.org/stable/common_pitfalls.html)
