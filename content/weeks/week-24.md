---
layout: week
week: 24
permalink: /weeks/week-24/
title: Project storytelling and mock interviews
description: Your project story needs to survive follow-up questions.
summary: Your project story needs to survive follow-up questions.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 24
kicker_secondary: 8 hours
---

## Start with the problem

Your project story needs to survive follow-up questions. A polished architecture slide helps only if you can explain what you personally decided, what evidence changed your mind and what remains incomplete. Build three versions of the same truthful account.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Tell the same story at three depths

**Think about this first.** What should fit in two minutes?

Start with the business problem, your role, the central design decision and the observed outcome. In ten minutes, add requirements, architecture, evaluation, deployment constraints and the main failure you addressed. In a deep dive, show evidence and defend trade-offs.

Keep the versions consistent. If a feature was a prototype in the deep dive, do not describe it as a production rollout in the short version. Avoid client names or sensitive operational details in external examples. Separate your contribution from shared team work without minimizing collaboration.

## 2. Bind claims to evidence

**Think about this first.** Can you defend a percentage without its denominator?

Every numerical claim needs a baseline, measurement period, sample or workload, metric definition and your contribution. Distinguish measured results from estimates, targets and plausible benefits. A model accuracy score is different from business savings; explain the link and its uncertainty.

Maintain a claim ledger: statement, evidence artifact, method, limitations and permitted audience. Use anonymized examples where needed. If the original measurement is unavailable, soften the statement rather than inventing a precise number. A reproducible failure and a clear correction can be stronger evidence of judgment than a perfect-looking demo.

## 3. Show leadership through decisions

**Think about this first.** What did you do when requirements were ambiguous?

Describe the situation, your responsibility, the options considered, your action and the result. Include why you rejected alternatives and how you handled disagreement. Good leadership examples show prioritization, communication, mentoring and response to evidence, not just technical complexity.

Prepare stories about scope reduction, a production issue, a failed experiment and a design disagreement. Avoid blaming colleagues. Explain what you learned and what process or test changed afterward. For role-fit questions, connect the target work to your actual strengths and the skills you are actively developing.

## Walk through one case

A demo agent failed on a missing contract. Instead of claiming the model was “unreliable,” you identified missing evidence, added an explicit unresolved outcome and created regression cases. The business benefit is better escalation behavior under a documented test set. Do not turn that evidence into an unmeasured claim about company-wide productivity.

## Guided practice

1. Write two-minute, ten-minute and deep-dive versions of one project.
2. Create a claim ledger with evidence and limitations for every metric.
3. Record a system-design mock and a debugging mock; ask follow-ups about sources, permissions, latency and failure recovery.
4. Prepare six leadership examples using real contributions and anonymized details.
5. Review the recording for unexplained jargon, vague ownership and unsupported outcomes. Revise the weak part rather than memorizing a longer script.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Prepare recruiter and hiring-manager answers about role expectations, remote work, availability and growth using accurate current facts. For technical follow-ups, be ready to defend chunking, embedding choice, workflow versus agent, evaluation units, cache scope, approvals, capacity and rollback. Say what you measured and what you would test next.

## Knowledge check

1. What must stay consistent across story lengths?
2. What supports a numerical claim?
3. How do you discuss a failed experiment?
4. Should an estimate be presented as an achievement?

### Answer key

1. Scope, personal ownership, implementation status and measured outcomes.
2. Metric definition, baseline, sample/workload, period and evidence.
3. Explain the hypothesis, observed failure, decision and resulting change.
4. No; label estimates and targets explicitly.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 25: Training foundations](/weeks/week-25/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [Google re:Work structured interviewing](https://rework.withgoogle.com/intl/en/guides/hiring-use-structured-interviewing)
- [Google SRE postmortem culture](https://sre.google/sre-book/postmortem-culture/)
