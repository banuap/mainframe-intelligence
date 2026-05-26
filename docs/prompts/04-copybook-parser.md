@workspace Read AGENTS.md and TEAM_BUILD_AND_DEPLOYMENT_GUIDE.md.

Implement Issue 4: Copybook Parser.

Files:
- app/ingestion/copybook_parser.py
- tests/test_ingestion.py
- data/samples/copybooks/TRADE-REC.cpy if needed

Parser should detect:
- 01-level records
- field names
- COBOL levels
- PIC clauses
- OCCURS if present

Return structured record and data element metadata.
Add tests.