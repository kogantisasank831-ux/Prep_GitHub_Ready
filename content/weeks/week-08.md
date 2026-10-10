---
layout: week
week: 8
permalink: /weeks/week-08/
title: Reranking and context construction
description: Your retriever finds the right catalogue, but the answer still uses a
  generic price.
summary: Your retriever finds the right catalogue, but the answer still uses a generic
  price.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 8
kicker_secondary: 8 hours
---

## Start with the problem

Your retriever finds the right catalogue, but the answer still uses a generic price. Search has not completely failed: the source was found and then lost before generation. This week follows that source through ranking, context selection and citations. Continue the same procurement corpus and source IDs from Week 7.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Candidate recall comes before reranking

**Think about this first.** Can a reranker recover a clause that was never retrieved?

Retrieval chooses a candidate set; reranking changes its order. A bi-encoder encodes query and document separately, allowing document vectors to be reused. A cross-encoder jointly processes each query–passage pair, adding work per candidate. Retrieve broadly enough to include useful evidence, then score a bounded set. Preserve original ranks and source revisions so the comparison can be explained.

A score is not necessarily a probability. Its meaning depends on the trained model and output transformation. Compare the same candidates before and after scoring. If you change retrieval depth as well, you have changed two factors. Measure candidate recall independently of final top-k quality.

## 2. Rewrite carefully and pack complete evidence

**Think about this first.** What does “CW-1000” become after a careless rewrite?

It can become generic copper-wire pricing and lose the exact product constraint. Retain the original question as a retrieval route. Preserve identifiers, dates, negations and supplier constraints in generated alternatives. Multi-query retrieval needs a cap, authorization on every route and fusion by stable source ID.

Count instructions, question, metadata, evidence and the actual chat template with the deployed tokenizer. Reserve output space before selecting passages. Deduplicate within a declared source/version policy. A table row that depends on a controlling section needs that section too; validate parent lineage and access before expanding it. Record omissions instead of silently truncating a payment condition.

## 3. Citations need support, not just an existing ID

**Think about this first.** Can a valid document ID accompany a false statement?

Yes. Validate both source identity and the claim it supports. Keep document revision, source digest and a stable span or location for each claim. “Net 30 after inspection approval” does not establish a calendar date without the approval date and a calculation policy. Compression must preserve the triggering condition.

Long-context position sensitivity is a reason to test evidence order, not a guarantee that moving a clause first solves reasoning. Compare fixed evidence under several orderings. Keep conflicting revisions visible when resolving the conflict is part of the task; do not let deduplication erase the disagreement.

## Walk through one case

Ask for the price of CW-1000. First find the catalogue in the full candidate list. Next inspect final top-k and then the actual context packet. If it disappears between those boundaries, improve selection before rewriting the answer prompt. Finally inspect the price claim and its cited span. Change one boundary at a time and retain the same labels. A supported abstention is preferable to inventing a price, but it still fails an answerable evaluation case.

## Guided practice

1. Save a fixed candidate list for ten questions, including exact-code and missing-evidence cases.
2. Add a scorer interface returning one finite score per passage; reject missing scores, duplicates and timeouts explicitly.
3. Pack whole passages under a full-prompt budget. Test a linked row, missing parent, revoked access and oversized instructions.
4. Compare hybrid-only and reranked results. Record candidate recall, final rank, evidence omissions and answer support.
5. Write one counterexample where reranking does not help. A heuristic exercise must be labeled as a heuristic; use a real cross-encoder only for a claimed neural comparison.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

HyDE embeds a generated hypothetical document to find real evidence; the hypothetical text is not a source. ColBERT uses token-level late interaction, unlike a jointly processed cross-encoder. Document-side hypothetical question expansion adds ingestion cost. Multi-hop retrieval makes a later lookup depend on verified earlier evidence. Self-RAG and CRAG are particular research designs; an ordinary self-check prompt does not reproduce them.

## Knowledge check

1. Why measure candidate recall first?
2. Why retain the original query?
3. What belongs in the token budget?
4. Does a resolving citation prove correctness?

### Answer key

1. A scorer cannot reorder evidence that is absent.
2. A rewrite can drop an exact identifier or change a condition.
3. The entire formatted input and reserved output, using the actual tokenizer/template.
4. No. The cited passage must support the claim and answer the actual question.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 9: RAG evaluation fundamentals](/weeks/week-09/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [Retrieve and re-rank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html)
- [Lost in the Middle](https://arxiv.org/abs/2307.03172)
