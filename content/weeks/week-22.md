---
layout: week
week: 22
permalink: /weeks/week-22/
title: MCP and interoperable tools
description: You have a useful supplier lookup and want more than one assistant to
  use it.
summary: You have a useful supplier lookup and want more than one assistant to use
  it.
published: true
status: reconstructed
version: 0.4.0
kicker_primary: Week 22
kicker_secondary: 8 hours
---

## Start with the problem

You have a useful supplier lookup and want more than one assistant to use it. A standard protocol can expose the capability consistently. It does not turn the lookup into a trusted authority or remove its authentication and data-access rules.

**Your eight-hour plan.** Use two hours for the concepts and source reading, three for the guided build, one for failure cases, one for interview practice and one for the knowledge check and your report. Keep larger framework, cloud or GPU extensions outside this minimum.

**What to carry forward.** Use the same procurement-assistant project, source identities and evaluation cases where relevant. The activities below are learner exercises: record what you actually run, keep failed cases, and do not treat a proposed build as an executed result.

## 1. Know the host, client and server roles

**Think about this first.** Which component decides whether a model may use a tool?

An MCP host manages the user experience and connections. A client maintains a protocol connection to a server. The server exposes capabilities such as tools, resources and prompts. Discovery tells a client what is available; availability is not permission to execute every operation.

Tools perform callable operations, resources expose contextual data, and prompts provide reusable interaction templates. Keep protocol transport separate from business logic. The same typed lookup service should enforce scope whether called through MCP, an HTTP API or a local test.

## 2. Negotiate compatibility and enforce boundaries

**Think about this first.** Can a client assume every optional capability exists?

No. Inspect the negotiated protocol/capabilities and the concrete SDK version. Optional features, transport and lifecycle behavior can change across releases. Record what you actually tested rather than claiming compatibility with every MCP host.

Authenticate at the transport boundary and authorize each resource/tool request. Avoid token passthrough that treats credentials intended for one audience as authority for another. Validate tool arguments and bound responses. Retrieved descriptions and tool output remain untrusted data for the consuming assistant.

## 3. Keep interoperability proportional to the problem

**Think about this first.** When is MCP unnecessary?

A single application with a direct internal function may not benefit from another protocol layer. MCP is useful when reusable capabilities need consistent discovery and access across hosts. Compare deployment, versioning and operational cost with the simpler interface.

A2A concerns agent-to-agent collaboration rather than merely calling a tool. Distinguish the task/agent boundary from the tool/data boundary. A protocol can make communication consistent without proving that a proposed action is safe, that an answer is supported or that a remote agent is competent.

## Walk through one case

Expose lookup_supplier as a read-only MCP tool. The caller provides a bounded supplier reference; the authenticated service supplies tenant scope. The server returns a bounded typed record with source version. A request for another tenant is denied even if a host's model claims it is urgent. The same denial should occur through the original service interface.

## Guided practice

1. Wrap one existing read-only capability with the official SDK.
2. Declare strict arguments and bounded results; keep identity outside model-controlled fields.
3. Test initialization, discovery, a successful call, invalid arguments and denied scope using a real client connection.
4. Exercise shutdown and malformed requests under the chosen transport.
5. Record protocol/SDK versions and optional capabilities. Label any HTTP, task or UI extension you have not tested.

## Independent challenge

Choose one assumption from the worked case and change it. Predict the first boundary that should fail before you run the experiment. Keep the original baseline and source versions, then explain the observed difference. Submit the smallest reproducible example and a test or review criterion that would catch the same failure again.

## Interview bridge

Explain tools/resources/prompts, host/client/server and capability negotiation. Describe the trust boundary and one case where a direct API is sufficient. Discuss A2A as a different abstraction rather than a replacement for authorization or tool contracts.

## Knowledge check

1. Is discovery authorization?
2. Who supplies tenant scope?
3. Should business logic live inside protocol handlers?
4. What does compatibility require?

### Answer key

1. No; the service must enforce access per operation.
2. The trusted authentication/application boundary.
3. Keep it reusable behind typed services, with thin transport adapters.
4. Recorded versions, negotiated capabilities and actual lifecycle/call tests.

## Definition of done

You can explain the three concepts without reading the page, work through the case with explicit assumptions, and present the guided activity with its actual outcome. Your report includes at least one failure, the first boundary responsible, a justified next change and the limits of your evidence. Answer every knowledge-check question and correct your notes after checking the explanations.

## Next connection

Continue to [Week 23: GenAI system design](/weeks/week-23/) and carry forward your source versions, tests and experiment notes.

## Primary sources

- [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
