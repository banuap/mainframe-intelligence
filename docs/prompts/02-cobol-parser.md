@workspace Read AGENTS.md and TEAM_BUILD_AND_DEPLOYMENT_GUIDE.md.

Implement Issue 2: COBOL Parser.

Files:
- app/ingestion/cobol_parser.py
- tests/test_ingestion.py
- data/samples/cobol/SETL001.cbl if needed

Parser should detect:
- PROGRAM-ID
- CALL statements
- COPY statements
- EXEC SQL blocks
- table references in SQL
- file references from SELECT, FD, READ, WRITE
- chunks with line numbers

Keep this heuristic-based for MVP. Add tests.