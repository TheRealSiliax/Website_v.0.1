## Boomerang-Loop (Delegation ↔ Reporting)

1) Task Execution: Agent führt zugewiesene Aufgabe fokussiert aus
2) Reporting: Agent liefert strukturierten Report (Reporter-Format)
3) Deliberation: Orchestrator/Team bewertet Fortschritt, lernt, plant nächste Schritte
4) Delegation: Orchestrator weist nächste Teilaufgabe dem passenden Agenten zu

Wiederholen, bis Akzeptanzkriterien erfüllt sind.

Verweise:
- Reporter-Format: `framework/templates/reporter.md`
- Task-Template: `framework/templates/task.md`

## Boomerang-Formulare (aus Intake)
```markdown
# Task Assignment (Orchestrator → Specialist)

## Task Context
[Project background and relationship to larger goals]

## Task Definition
[Specific work to be completed]

## Expected Output
[Detailed description of deliverables]

## Return Instructions
When complete, explicitly return to Orchestrator with:
- Summary of completed work
- Links to deliverables
- Issues encountered
- Recommendations for next steps

## Meta-Information
- task_id: [UNIQUE_ID]
- origin: Orchestrator
- destination: [Specialist]
- boomerang_return_to: Orchestrator
```

```markdown
# Task Return (Specialist → Orchestrator)

## Task Completion
Task [ID] has been completed.

## Deliverables
[Links or references to outputs]

## Issues Encountered
[Problems, limitations, or challenges]

## Next Steps
[Recommendations for follow-up work]

## Meta-Information
- task_id: [ID]
- origin: [Specialist]
- destination: Orchestrator
- status: completed
```


