# Mainframe Application Intelligence Platform

This project builds an ontology-driven intelligence layer for mainframe relearning and modernization.

It ingests COBOL, JCL, copybooks, and documentation, then creates:

- PostgreSQL ontology store
- ChromaDB semantic search index
- NetworkX runtime dependency graph
- FastAPI agent tool layer
- Mock/Vertex AI LLM interface

The goal is to help teams and agents answer modernization questions such as:

- What does this program do?
- What jobs execute this program?
- What data does it read and write?
- What rules does it implement?
- What business capability does it support?
- What is impacted if this logic changes?
- What should be modernized into a service/API?

## Architecture

```text
Mainframe Assets
COBOL | JCL | Copybooks | DB2 DDL | VSAM layouts | Docs | Runbooks
        |
        v
Parser / Extractor / Gemini-based Classifier
        |
        v
PostgreSQL Ontology Store
        |
        +----------------------+
        |                      |
        v                      v
ChromaDB / Vertex AI Search    Vertex AI / Gemini
Semantic retrieval             Reasoning + agents
        |
        v
Agents / Apps / Modernization Factory
```

## Step 1 contents

This repository currently contains the initial scaffold:

- `AGENTS.md` with Codex build instructions
- `requirements.txt`
- `.env.example`
- FastAPI app skeleton
- PostgreSQL schema stub
- ontology seed script stub
- parser module stubs
- agent, graph, and vector store placeholders
- sample data folders
- initial tests

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Run API

```bash
uvicorn app.main:app --reload
```

Health check:

```bash
curl http://localhost:8000/health
```

## Run tests

```bash
pytest
```

## Database

Create the schema:

```bash
psql "$DATABASE_URL" -f app/db/schema.sql
```

Seed the core ontology classes and relationship types:

```bash
python -m app.db.seed_ontology
```

## Next milestone

Step 2 should implement:

- PostgreSQL connection handling
- repository functions for ontology objects and relationships
- real schema creation
- seed ontology script
- initial ingestion of sample COBOL/JCL/copybooks



## Issues in github

- Issue 1: Implement PostgreSQL Ontology Repository
- Issue 2: Implement COBOL Parser
- Issue 3: Implement JCL Parser
- Issue 4: Implement Copybook Parser
- Issue 5: Implement Ingestion Pipeline
- Issue 6: Implement NetworkX Graph Loader
- Issue 7: Implement Agent Tools
- Issue 8: Implement Vertex AI Provider

- example: 
- @workspace Implement GitHub Issue 1 using docs/prompts/01-postgres-ontology-repository.md.

- or 
- @workspace Read docs/prompts/01-postgres-ontology-repository.md and implement it. Follow .github/copilot-instructions.md.