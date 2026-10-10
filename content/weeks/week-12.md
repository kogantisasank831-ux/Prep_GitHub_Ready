---
layout: week
week: 12
permalink: /weeks/week-12/
title: Deploying the RAG service
description: The assistant works in a notebook.
summary: The assistant works in a notebook.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 12
kicker_secondary: 8 hours
---

## Start with the problem

The assistant works in a notebook. Now two people upload documents while a third asks a question during an index refresh. Deployment exposes ownership, lifecycle and resource assumptions that a single-user demo hides. Turn those assumptions into explicit service contracts.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Choose the service boundaries

**Think about this first.** Should a chat request parse a large document synchronously?

Usually ingestion and interactive answering need different resource policies. Validate the upload, create a job identity and perform expensive parsing/indexing in bounded workers. Record progress and a corpus revision. Answer against a complete published revision rather than a half-built index.

Keep request contracts typed and errors stable. Separate liveness from readiness: a live process may not be ready to answer without its index or dependencies. Do not use a health endpoint that triggers costly model generation. Bound request size, queue length, concurrency and deadlines according to measured capacity.

## 2. Package configuration and state deliberately

**Think about this first.** What disappears when a container restarts?

Anything stored only in its ephemeral filesystem or process memory. Place durable metadata, document objects and indexes in appropriate persistent stores. Supply credentials through a secret mechanism rather than the image. Pin dependencies and model artifacts, record licenses and use a minimal runtime user.

A reproducible release binds code, prompt/configuration, model and source/index revisions. Keep startup migrations and rollback behavior explicit. Rolling back code alone does not necessarily roll back an incompatible database or index format. Begin locally before adding orchestration complexity.

## 3. Measure the whole deployment path

**Think about this first.** Does one fast model request establish service capacity?

No. Include upload/queue time, retrieval, reranking, network, decoding and client-visible latency under a declared workload. Measure concurrent active requests rather than registered users. Check p95 latency, errors, saturation and resource headroom as load rises.

Cloud design includes identity, private network paths, storage location, backup/restore and egress. A Kubernetes deployment adds operational controls, not automatic application correctness. Define readiness, termination grace, bounded work and autoscaling signals that match the bottleneck. Scale workers independently if ingestion competes with interactive traffic.

## Walk through one case

Publish index revision B while requests use revision A. Construct and validate B separately, then atomically switch the active pointer. An in-flight request retains its selected revision so citations remain explainable. Keep A until the rollback/retention policy permits deletion. If B fails validation, leave the pointer at A and show the failed ingestion job.

## Guided practice

1. Containerize the existing typed service and document its environment settings.
2. Add liveness/readiness endpoints with distinct meanings and no expensive side effects.
3. Separate ingestion jobs from interactive requests and publish an index revision atomically.
4. Test restart, dependency outage, concurrent uploads and shutdown during a request.
5. Record a reproducible local load run and an explicit rollback procedure. Optional cloud deployment should follow the same tested contracts.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

For enterprise RAG, explain identity and network boundaries, object storage, metadata/index consistency, job processing, admission control, observability and recovery. Map the architecture to AWS, Azure or GCP services only after the responsibilities are clear. A service-name list is not a capacity or reliability argument.

## Knowledge check

1. Why separate ingestion and answering?
2. What does readiness mean?
3. Why bind a request to an index revision?
4. What must a rollback account for?

### Answer key

1. Their latency, memory and concurrency needs differ.
2. The instance has the required dependencies/state to serve its declared traffic.
3. To keep retrieval and citations consistent across refreshes.
4. Code, schemas, configuration and artifact/index compatibility.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 13: Tool calling](/weeks/week-13/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [FastAPI deployment concepts](https://fastapi.tiangolo.com/deployment/concepts/)
- [Kubernetes probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
