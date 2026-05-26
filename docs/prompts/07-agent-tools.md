@workspace Read AGENTS.md and TEAM_BUILD_AND_DEPLOYMENT_GUIDE.md.

Implement Issue 7: API Agent Tools.

Files:
- app/agents/tools.py
- app/api/routes.py
- app/agents/mainframe_agent.py
- tests/

Implement tools:
- get_program_summary
- get_program_dependencies
- get_program_business_rules
- get_job_flow
- get_impacted_assets
- search_source_evidence
- get_modernization_candidates
- generate_impact_assessment

Do not allow arbitrary SQL.
Return structured evidence.
Add tests.