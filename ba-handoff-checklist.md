# BA Handoff Checklist for COBOL-to-Java Modernization with Domain-Driven Design

This checklist is designed for business analysts who are taking over from architecture, engineering, and reverse-engineering teams during a mainframe modernization effort. It assumes the current-state discovery has already produced application inventories, dependency maps, business-rule extraction, and candidate domain decomposition inputs. Research on use cases, BA handoff quality, event storming, and legacy modernization consistently emphasizes clear business context, actors, goals, scenarios, exceptions, assumptions, dependencies, and open questions as the minimum handoff baseline.[cite:16][cite:19][cite:22][cite:24][cite:27]

## Purpose

Use this checklist to confirm that the BA team has enough structured information to begin writing future-state use cases, user stories, acceptance criteria, and bounded-context-aligned requirements. Well-prepared handoffs reduce misinterpretation, preserve business context, document assumptions, and make downstream analysis testable and traceable.[cite:19][cite:20]

## How to Use This Checklist

- Treat each major business process or subdomain as a separate handoff package.
- Mark every line as Complete, Partial, Not Available, or Not Applicable.
- Add evidence links for each completed item, such as program inventory, workshop notes, process maps, copybook analysis, or SME validation.
- Keep inferred content separate from confirmed content.
- Record unresolved questions in a visible backlog before BA story-writing begins.[cite:19][cite:22][cite:25]

## Handoff Readiness

- [ ] Modernization scope is defined at business-domain level, not only by application or program boundaries.[cite:24][cite:27]
- [ ] In-scope business capabilities are listed and prioritized.[cite:24][cite:27]
- [ ] Out-of-scope capabilities and deferred functions are explicitly listed.
- [ ] The modernization objective is clear for each scope item: preserve, simplify, redesign, automate, or retire.[cite:21][cite:24]
- [ ] Target-state intent is documented: functional equivalence, partial redesign, or full business-process transformation.[cite:21][cite:24]
- [ ] Stakeholder groups are identified, including business owners, operations, compliance, customer-support users, and downstream consumers.[cite:20][cite:27]
- [ ] SME contacts are named for each major process or rule area.[cite:22][cite:25]

## Business Context

- [ ] The business outcome of each process is stated in plain language.
- [ ] The business value of the process is documented, such as revenue impact, regulatory obligation, risk control, customer service, or operational continuity.[cite:24][cite:27]
- [ ] Triggering events are identified, including user actions, inbound files, messages, schedules, or external requests.[cite:22][cite:25]
- [ ] The initiating actor is identified for each trigger.[cite:16][cite:18]
- [ ] The end condition or success outcome is defined for each process.[cite:16][cite:18]
- [ ] Process frequency, timing, and critical operational windows are recorded.[cite:24]
- [ ] Any seasonal, month-end, quarter-end, or regulatory timing sensitivity is documented.

## Current-State Process Coverage

- [ ] A current-state process flow exists for each major capability.
- [ ] The main success path is documented step by step.[cite:16][cite:18]
- [ ] Alternate paths are documented.[cite:16]
- [ ] Exception and failure paths are documented.[cite:16][cite:19]
- [ ] Manual workarounds and operator interventions are documented.
- [ ] Batch and online variants of the process are separated where behavior differs.
- [ ] Upstream and downstream dependencies are identified for each step.[cite:24][cite:27]
- [ ] Known dead code, obsolete branches, or rarely used flows are flagged for validation.

## Use Case Inputs

- [ ] Each use case has a clear name based on an actor goal.[cite:16][cite:18]
- [ ] Primary actor is identified.[cite:16]
- [ ] Supporting actors and external systems are identified.[cite:16]
- [ ] Preconditions are documented.
- [ ] Postconditions are documented.
- [ ] Trigger is documented.
- [ ] Main flow is written in business language rather than technical implementation language.[cite:16][cite:18]
- [ ] Alternate flows are linked to the main flow steps.[cite:16]
- [ ] Exceptions are linked to the relevant failure point.[cite:16]
- [ ] Business rules referenced by the use case are linked by ID.
- [ ] Required data inputs and outputs are listed.
- [ ] Audit, approval, or compliance obligations are attached where relevant.[cite:24][cite:27]

## Domain and DDD Inputs

- [ ] Candidate bounded contexts are identified.[cite:25]
- [ ] Subdomains are identified and labeled as core, supporting, or generic where possible.[cite:25]
- [ ] Commands are identified as business actions that cause outcomes.[cite:25]
- [ ] Domain events are named in past tense and linked to the process timeline.[cite:22][cite:25]
- [ ] Aggregates or core business objects are identified where behavior clusters around consistency boundaries.[cite:25]
- [ ] Views or user-facing tasks needed to support the workflow are identified.[cite:25]
- [ ] Candidate context boundaries are reviewed for ownership, policy differences, and integration points.[cite:25]
- [ ] Ubiquitous language terms are proposed for future-state usage.

## Business Rules

- [ ] Business rules are extracted and normalized from the legacy logic.[cite:24][cite:27]
- [ ] Each rule has an ID and short name.
- [ ] Each rule is classified, such as eligibility, validation, calculation, routing, compliance, or notification.
- [ ] Rule source is traceable to program, paragraph, copybook, file layout, screen, report, or SME statement.
- [ ] Conditions and outcomes are documented explicitly.
- [ ] Thresholds, tolerances, and default values are recorded.
- [ ] Override behavior is documented.
- [ ] Rule conflicts or ambiguities are flagged for workshop review.[cite:19]
- [ ] Rules suspected to be technical rather than business rules are separated.

## Data and Information Model

- [ ] Core business entities are identified.
- [ ] Legacy names are mapped to business-friendly names.
- [ ] Key attributes are described in business language.
- [ ] Record lifecycle or status transitions are documented.
- [ ] System of record is identified for each major data object.[cite:24]
- [ ] Input sources and output consumers are listed.
- [ ] Data quality issues and known anomalies are documented.[cite:24]
- [ ] Retention, privacy, masking, or regulatory handling needs are noted.[cite:24]
- [ ] Cross-system identifier mappings are documented.

## Integration and Operations

- [ ] Interface inventory is provided, including files, APIs, queues, screens, jobs, and reports.[cite:24][cite:27]
- [ ] Interface direction is documented as inbound, outbound, or bidirectional.
- [ ] Message or file trigger conditions are documented.
- [ ] SLA, cutoff, or batch window dependencies are documented.[cite:24]
- [ ] Restart, replay, reconciliation, and recovery needs are documented.
- [ ] Operational monitoring or alerting expectations are documented.
- [ ] Human operational roles are identified for exception handling.
- [ ] Business continuity or fallback procedures are documented if they exist.

## Assumptions and Gaps

- [ ] Every inferred statement is marked as inferred.
- [ ] Confidence level is assigned to extracted logic where validation is pending.
- [ ] Open questions are captured in a single tracked list.[cite:19]
- [ ] Conflicting behaviors across sources are documented.
- [ ] Missing SME validation areas are highlighted.
- [ ] Missing artifacts are called out explicitly rather than silently skipped.[cite:19]
- [ ] Decisions already made are documented with owner and date.[cite:19]

## Story-Writing Readiness

- [ ] Processes can be decomposed into user-goal-oriented use cases.[cite:16][cite:18]
- [ ] Use cases can be decomposed into stories without losing end-to-end traceability.[cite:17]
- [ ] Acceptance criteria can be derived from process steps, rules, and exceptions.[cite:17]
- [ ] Story boundaries align to bounded contexts or coherent workflow slices.[cite:25]
- [ ] Cross-context dependencies are visible before backlog creation.[cite:25]
- [ ] Non-functional concerns are noted where they materially affect requirements, such as auditability, performance windows, security, resiliency, or explainability.[cite:21][cite:24]
- [ ] A backlog seed list exists for epics, use cases, and candidate stories.

## Recommended Handoff Artifacts

Attach or link these artifacts to the repository folder that contains this checklist:

- Process inventory spreadsheet.
- Capability-to-process mapping.
- Event catalog.
- Business rules catalog.
- Domain glossary and ubiquitous language draft.
- Current-state workflow diagrams.
- Interface and dependency map.
- Data dictionary or canonical data-object sheet.
- Assumptions, decisions, and open-questions log.
- SME validation notes and workshop outputs.[cite:20][cite:22][cite:25][cite:27]

## Suggested Repository Structure

```text
ba-handoff/
├── README.md
├── checklist/
│   └── ba-handoff-checklist.md
├── process-inventory/
├── capability-maps/
├── workflows/
├── domain-model/
├── business-rules/
├── data-dictionary/
├── interfaces/
├── decisions-and-assumptions/
└── workshops-and-validation/
```

## Minimal Use Case Template

Use the following template when converting handoff material into BA use cases:

```md
# Use Case: <Name>

## Goal
<Business outcome>

## Primary Actor
<Actor>

## Supporting Actors / Systems
<List>

## Trigger
<Event, command, schedule, or request>

## Preconditions
<List>

## Postconditions
<List>

## Main Flow
1. ...
2. ...
3. ...

## Alternate Flows
- ...

## Exception Flows
- ...

## Business Rules
- BR-001 ...

## Data
- Inputs:
- Outputs:

## Dependencies
- Upstream:
- Downstream:

## Open Questions
- ...
```

## Definition of Ready for BA Start

The BA team is ready to begin future-state use case and story creation when each in-scope process has a named business outcome, known actors, triggers, main and exception flows, linked business rules, core data objects, integration touchpoints, and a visible list of unresolved questions. That level of completeness aligns with practical use-case guidance, event-storming preparation, and modernization planning practices that emphasize clarity of goals, scenarios, dependencies, assumptions, and stakeholder context before detailed requirements work begins.[cite:16][cite:19][cite:22][cite:24][cite:27]
