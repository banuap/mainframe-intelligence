@workspace Read AGENTS.md and TEAM_BUILD_AND_DEPLOYMENT_GUIDE.md.

Implement Issue 5: Ingestion Pipeline.

Files:
- app/ingestion/ingest_pipeline.py
- app/api/routes.py
- app/ontology/repository.py if needed
- app/vectorstore/chroma_store.py if needed
- tests/test_ingestion.py

The ingestion pipeline should:
1. Walk a directory recursively
2. Classify files as COBOL, JCL, copybook, or documentation
3. Parse each file
4. Persist source artifacts
5. Persist artifact chunks
6. Persist ontology objects
7. Persist ontology relationships
8. Store chunks in ChromaDB if configured

Update POST /ingest/path to call the real pipeline.
Add tests.