@workspace Read AGENTS.md and TEAM_BUILD_AND_DEPLOYMENT_GUIDE.md.

Implement Issue 3: JCL Parser.

Files:
- app/ingestion/jcl_parser.py
- tests/test_ingestion.py
- data/samples/jcl/EODSETL.jcl if needed

Parser should detect:
- JOB name
- EXEC PGM
- step names
- PROC usage
- DD dataset references

Return structured parse result with job name, steps, executed programs, and datasets.
Add tests.