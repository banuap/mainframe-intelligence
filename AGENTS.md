# AGENTS.md

## Project name

Mainframe Application Intelligence Platform

## Goal

Build a Python-based MVP that ingests mainframe assets such as COBOL, JCL, copybooks, and documentation, extracts application intelligence, stores ontology objects and relationships in PostgreSQL, stores semantic chunks in ChromaDB, loads runtime graphs into NetworkX, and exposes agent tools for mainframe relearning and modernization.

## Business purpose

The platform helps teams relearn and modernize legacy mainframe applications by creating a shared application intelligence layer.

The intelligence layer should answer questions such as:

- What does this COBOL program do?
- Which JCL jobs execute this program?
- Which copybooks and data elements does it use?
- Which business rules are implemented in this code?
- Which business capabilities does this program support?
- What is impacted if a business rule, data element, or program changes?
- What modernization candidates should become APIs or target services?
- What regression tests are needed for a proposed change?

## Technology constraints

Use only the following core technologies for the MVP:

- Python
- PostgreSQL
- SQLAlchemy or psycopg2
- NetworkX
- ChromaDB
- FastAPI
- Pydantic
- Vertex AI / Gemini integration placeholder interfaces
- Optional: LlamaIndex or LangChain only if needed

Do not add Neo4j, TigerGraph, Neptune, Kafka, or cloud-specific dependencies unless explicitly requested.

## Architecture

The architecture has five layers:

1. Ingestion Layer
   - Reads COBOL, JCL, copybooks, DDL, and documentation.
   - Splits files into chunks.
   - Extracts metadata such as program names, job steps, copybooks, file references, table references, and possible business rules.

2. Ontology Store
   - PostgreSQL stores ontology classes, ontology objects, relationship types, relationships, source artifacts, and chunks.
   - PostgreSQL is the persistent system of record.

3. Vector Store
   - ChromaDB stores semantic chunks for COBOL, JCL, copybooks, and documentation.
   - Each chunk must include metadata such as artifact name, artifact type, object id, line start, line end, and business domain if known.

4. Runtime Graph
   - NetworkX loads ontology relationships from PostgreSQL.
   - It supports graph traversal, dependency analysis, impact analysis, upstream/downstream queries, centrality, and modernization risk analysis.

5. Agent Tool Layer
   - FastAPI exposes controlled tools for agents.
   - Agents should not issue arbitrary SQL.
   - Tools call PostgreSQL, ChromaDB, NetworkX, and Vertex AI/Gemini interfaces.

## Ontology model

Implement the following ontology classes:

- Application
- Program
- JCLJob
- JCLStep
- Copybook
- DataElement
- DB2Table
- VSAMFile
- CICSMap
- Transaction
- BusinessRule
- BusinessCapability
- BatchFlow
- Interface
- Report
- TestCase
- TargetService
- ModernizationCandidate

Implement the following relationship types:

- CALLS
- EXECUTES
- HAS_STEP
- USES_COPYBOOK
- DEFINES
- READS
- WRITES
- IMPLEMENTS
- SUPPORTS
- PART_OF
- PRODUCES
- CONSUMES
- MAPS_TO
- MODERNIZES_TO
- TESTED_BY
- IMPACTS
- DEPENDS_ON

## PostgreSQL tables

Create schema for:

- ontology_class
- ontology_object
- relationship_type
- ontology_relationship
- source_artifact
- artifact_chunk
- modernization_score
- agent_query_log

## API tools to expose

Implement these API endpoints:

- POST /ingest/path
- GET /program/{program_name}/summary
- GET /program/{program_name}/dependencies
- GET /program/{program_name}/business-rules
- GET /job/{job_name}/flow
- GET /impact/program/{program_name}
- GET /impact/rule/{rule_name}
- GET /impact/data-element/{data_element_name}
- POST /search/evidence
- POST /modernization/candidates
- POST /agent/ask

## Agent behavior

The agent should answer using this sequence:

1. Determine whether the question is about source evidence, graph relationships, or modernization reasoning.
2. Retrieve relevant ontology objects from PostgreSQL.
3. Retrieve relevant source chunks from ChromaDB.
4. Use NetworkX for dependency or impact traversal where needed.
5. Use Gemini or a placeholder LLM interface to synthesize a final answer.
6. Include evidence references when possible: artifact name, line range, object name, relationship path.

## Coding standards

- Use clear, modular Python.
- Use type hints.
- Use Pydantic models for API contracts.
- Use environment variables for DB and model configuration.
- Keep provider-specific LLM code behind an interface.
- Do not hardcode credentials.
- Add unit tests for parser, ontology repository, vector store wrapper, and impact analyzer.
- Prefer simple working MVP over overly abstract framework design.

## Commands

Install:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run database schema:

```bash
psql "$DATABASE_URL" -f app/db/schema.sql
```

Seed ontology:

```bash
python -m app.db.seed_ontology
```

Run API:

```bash
uvicorn app.main:app --reload
```

Run tests:

```bash
pytest
```

## Definition of done for MVP

The MVP is done when:

1. Sample COBOL, JCL, and copybook files can be ingested.
2. PostgreSQL stores ontology objects and relationships.
3. ChromaDB stores searchable chunks with metadata.
4. NetworkX can load the graph from PostgreSQL.
5. API can answer:
   - program dependencies
   - job flow
   - business rule mapping
   - impact analysis
   - evidence search
6. `/agent/ask` can combine ontology, graph traversal, and vector evidence into a useful answer.
7. Tests pass.

## First implementation order

Build in this order:

1. requirements.txt
2. PostgreSQL schema.sql
3. database connection
4. seed ontology classes and relationship types
5. parser stubs for COBOL, JCL, copybook
6. ingestion pipeline
7. ontology repository
8. ChromaDB wrapper
9. NetworkX graph loader and impact analyzer
10. FastAPI routes
11. agent tools
12. sample data
13. tests
14. README
