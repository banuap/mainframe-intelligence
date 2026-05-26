# Mainframe Application Intelligence Platform — Team Build & Deployment Guide

## 1. Purpose

This repository builds a **Mainframe Application Intelligence Platform**.

The goal is to help teams relearn, understand, and modernize mainframe applications by creating a shared intelligence layer from:

- COBOL programs
- JCL jobs
- Copybooks
- DB2 DDL
- VSAM layouts
- Documentation
- Runbooks
- Test cases
- Business rules

The platform stores this intelligence in:

- **PostgreSQL** for ontology objects, relationships, metadata, and governance
- **ChromaDB or Vertex AI Search** for semantic search over code and documentation
- **NetworkX** for graph traversal and impact analysis
- **Vertex AI / Gemini** for reasoning, summarization, extraction, and agent responses
- **FastAPI** for API and agent tool access

---

## 2. Target Architecture

```text
Mainframe Assets
COBOL | JCL | Copybooks | DB2 DDL | VSAM | Docs | Runbooks
        |
        v
Ingestion + Parsing + Gemini Extraction
        |
        v
Application Intelligence Layer
-----------------------------------------------------
| PostgreSQL Ontology Store                         |
|   - Programs                                      |
|   - Jobs                                          |
|   - Copybooks                                     |
|   - Data elements                                 |
|   - Business rules                                |
|   - Business capabilities                         |
|   - Relationships                                 |
|   - Modernization scores                          |
|                                                   |
| Vector Search                                     |
|   - ChromaDB for local MVP                        |
|   - Vertex AI Search for enterprise deployment    |
|                                                   |
| Runtime Graph                                     |
|   - NetworkX graph loaded from PostgreSQL         |
-----------------------------------------------------
        |
        v
FastAPI Agent Tool Layer
        |
        v
Agents / Dashboards / Modernization Factory
```

---

## 3. Repository Setup

### 3.1 Create the GitHub repository

Create a new GitHub repository:

```text
banuap/mainframe-intelligence
```

Recommended settings:

- Visibility: Private
- Add README: No, if pushing from local scaffold
- Add .gitignore: No, already included
- Add license: Optional

---

### 3.2 Clone or initialize locally

If the repo already exists:

```bash
git clone https://github.com/banuap/mainframe-intelligence.git
cd mainframe-intelligence
```

If starting from the local scaffold:

```bash
cd C:\Users\banu.parasuraman\Downloads\mainframe-intelligence
git init
git remote add origin https://github.com/banuap/mainframe-intelligence.git
git branch -M main
git add .
git commit -m "Initial mainframe intelligence platform scaffold"
git push -u origin main
```

If GitHub already has a README and the push is rejected:

```bash
git pull origin main --allow-unrelated-histories
git checkout --ours README.md
git add README.md
git commit -m "Merge remote main and keep project scaffold README"
git push -u origin main
```

---

## 4. Recommended Repository Structure

```text
mainframe-intelligence/
  AGENTS.md
  README.md
  TEAM_BUILD_AND_DEPLOYMENT_GUIDE.md
  requirements.txt
  .env.example
  .gitignore

  app/
    main.py
    config.py

    api/
      routes.py

    db/
      connection.py
      schema.sql
      seed_ontology.py

    ingestion/
      cobol_parser.py
      jcl_parser.py
      copybook_parser.py
      chunker.py
      ingest_pipeline.py

    ontology/
      models.py
      repository.py
      graph_loader.py
      impact_analyzer.py

    vectorstore/
      chroma_store.py
      embeddings.py

    agents/
      prompts.py
      tools.py
      mainframe_agent.py
      llm.py

  data/
    samples/
      cobol/
      jcl/
      copybooks/

  tests/
    test_health.py
    test_ingestion.py
    test_ontology.py
    test_impact_analysis.py

  deploy/
    Dockerfile
    docker-compose.yml
    cloudrun/
    terraform/
```

---

## 5. Local Developer Setup

### 5.1 Create virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Mac/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

---

### 5.2 Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5.3 Create local environment file

```bash
copy .env.example .env
```

Mac/Linux:

```bash
cp .env.example .env
```

Update `.env`:

```env
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/mainframe_intelligence
CHROMA_PATH=.chroma
CHROMA_COLLECTION=mainframe_chunks
GOOGLE_CLOUD_PROJECT=<your-gcp-project-id>
GOOGLE_CLOUD_LOCATION=us-central1
VERTEX_MODEL_NAME=gemini-1.5-pro
EMBEDDING_MODEL_NAME=text-embedding-004
APP_ENV=local
```

---

## 6. Local PostgreSQL Setup

### Option A: Use local PostgreSQL

Create database:

```sql
CREATE DATABASE mainframe_intelligence;
```

Run schema:

```bash
psql "$DATABASE_URL" -f app/db/schema.sql
```

On Windows, if using normal psql connection format:

```bash
psql postgresql://postgres:postgres@localhost:5432/mainframe_intelligence -f app/db/schema.sql
```

Seed ontology:

```bash
python -m app.db.seed_ontology
```

---

### Option B: Use Docker PostgreSQL

Add this later as `deploy/docker-compose.yml`:

```yaml
version: "3.9"

services:
  postgres:
    image: postgres:16
    container_name: mainframe-intelligence-postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: mainframe_intelligence
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

Run:

```bash
docker compose -f deploy/docker-compose.yml up -d
```

Then:

```bash
psql postgresql://postgres:postgres@localhost:5432/mainframe_intelligence -f app/db/schema.sql
python -m app.db.seed_ontology
```

---

## 7. Run the API Locally

```bash
uvicorn app.main:app --reload
```

Health check:

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{
  "status": "ok",
  "app": "Mainframe Application Intelligence Platform",
  "env": "local"
}
```

Interactive API docs:

```text
http://localhost:8000/docs
```

---

## 8. Run Tests

```bash
pytest
```

Before every commit:

```bash
pytest
```

Optional:

```bash
pytest -q
```

---

## 9. Git Workflow for the Team

### 9.1 Branch strategy

Use:

```text
main
  Stable branch

develop
  Integration branch

feature/*
  Individual feature work

bugfix/*
  Fixes

release/*
  Release stabilization
```

Example:

```bash
git checkout -b develop
git push -u origin develop
```

Feature branch:

```bash
git checkout develop
git pull
git checkout -b feature/postgres-ontology-repository
```

Commit:

```bash
git add .
git commit -m "Implement PostgreSQL ontology repository"
git push -u origin feature/postgres-ontology-repository
```

Open a pull request:

```text
feature/postgres-ontology-repository -> develop
```

After review, merge into `develop`.

Promote to `main` after integration testing.

---

## 10. Issue Backlog

Create these GitHub issues.

---

### Issue 1: Implement PostgreSQL Ontology Repository

**Goal**

Make PostgreSQL the persistent ontology store.

**Tasks**

- Complete database connection handling
- Implement SQLAlchemy session management
- Implement `OntologyRepository`
- Implement object upsert
- Implement relationship upsert
- Implement lookup by object name
- Implement relationship query by object
- Add tests

**Acceptance Criteria**

- `pytest` passes
- Objects can be inserted and read
- Relationships can be inserted and read
- Seed script works

---

### Issue 2: Implement COBOL Parser

**Goal**

Extract useful intelligence from COBOL programs.

**Tasks**

- Detect `PROGRAM-ID`
- Detect `CALL` statements
- Detect `COPY` statements
- Detect `EXEC SQL`
- Detect table references
- Detect file references
- Chunk source by section or paragraph
- Add tests using sample COBOL

**Acceptance Criteria**

- Parser extracts program name
- Parser extracts called programs
- Parser extracts copybooks
- Parser returns chunks with line numbers

---

### Issue 3: Implement JCL Parser

**Goal**

Extract job flow intelligence from JCL.

**Tasks**

- Detect job name
- Detect `EXEC PGM`
- Detect steps
- Detect DD datasets
- Create job-step-program relationships
- Add tests using sample JCL

**Acceptance Criteria**

- Parser extracts job name
- Parser extracts steps
- Parser extracts executed programs
- Parser extracts dataset references

---

### Issue 4: Implement Copybook Parser

**Goal**

Extract data records and data elements from copybooks.

**Tasks**

- Detect 01-level records
- Detect field names
- Detect PIC clauses
- Detect nested levels
- Create Copybook and DataElement objects
- Add tests

**Acceptance Criteria**

- Parser extracts record names
- Parser extracts data elements
- Parser preserves level and PIC metadata

---

### Issue 5: Implement Ingestion Pipeline

**Goal**

Ingest a folder of mainframe files and populate ontology + vector store.

**Tasks**

- Walk directory recursively
- Classify files by extension/content
- Call COBOL, JCL, copybook parsers
- Persist source artifacts
- Persist chunks
- Persist ontology objects
- Persist relationships
- Store chunks in ChromaDB
- Add tests

**Acceptance Criteria**

- `POST /ingest/path` ingests sample directory
- PostgreSQL contains objects and relationships
- ChromaDB contains chunks
- Evidence metadata includes line numbers

---

### Issue 6: Implement NetworkX Graph Loader

**Goal**

Load the ontology graph from PostgreSQL into NetworkX.

**Tasks**

- Load ontology objects as nodes
- Load relationships as directed edges
- Preserve node metadata
- Preserve relationship metadata
- Add graph traversal utilities
- Add tests

**Acceptance Criteria**

- Graph loads from repository
- Downstream traversal works
- Upstream traversal works
- Shortest path works

---

### Issue 7: Implement Impact Analyzer

**Goal**

Answer impact analysis questions.

**Tasks**

- Implement downstream impact
- Implement upstream dependency
- Implement path analysis
- Implement high-risk nodes using degree centrality
- Add API endpoints
- Add tests

**Acceptance Criteria**

- `/impact/program/{program_name}` returns impacted assets
- `/impact/rule/{rule_name}` returns impacted assets
- `/impact/data-element/{data_element_name}` returns impacted assets

---

### Issue 8: Implement ChromaDB Vector Store

**Goal**

Enable semantic search over code and documentation chunks.

**Tasks**

- Implement ChromaDB wrapper
- Add chunks with metadata
- Search chunks by text
- Filter by metadata
- Add mock embeddings or local embeddings for MVP
- Add tests

**Acceptance Criteria**

- Chunks can be added
- Chunks can be searched
- Metadata filters work
- Results include artifact name and line range

---

### Issue 9: Implement Agent Tools

**Goal**

Expose safe tools for agents.

**Tasks**

Implement:

- `get_program_summary`
- `get_program_dependencies`
- `get_program_business_rules`
- `get_job_flow`
- `get_impacted_assets`
- `search_source_evidence`
- `get_modernization_candidates`
- `generate_impact_assessment`

**Acceptance Criteria**

- Tools do not expose arbitrary SQL
- Tools use repository, graph, and vector store
- Tools return structured evidence

---

### Issue 10: Implement `/agent/ask`

**Goal**

Allow users to ask natural language questions.

**Tasks**

- Classify user intent
- Route to correct tools
- Retrieve ontology facts
- Retrieve evidence chunks
- Run graph analysis if needed
- Use mock LLM first
- Add Vertex AI / Gemini provider later

**Acceptance Criteria**

- Agent can answer:
  - What does SETL001 do?
  - What jobs execute SETL001?
  - What copybooks does SETL001 use?
  - What is impacted if SETL001 changes?
  - What business rules are related to settlement?

---

### Issue 11: Add Vertex AI / Gemini Integration

**Goal**

Use Gemini for summarization, extraction, and response generation.

**Tasks**

- Implement LLM provider interface
- Implement mock provider
- Implement Vertex AI Gemini provider
- Implement extraction prompts
- Implement answer synthesis prompts
- Use environment variables
- Avoid hardcoded credentials

**Acceptance Criteria**

- Tests use mock provider
- Local dev can use mock provider
- GCP deployment can use Vertex AI provider

---

### Issue 12: Add Dockerfile and Deployment Packaging

**Goal**

Package the API for deployment.

**Tasks**

- Add Dockerfile
- Add docker-compose for local PostgreSQL
- Add startup command
- Add environment variable documentation
- Add health check

**Acceptance Criteria**

- Docker image builds
- Container starts locally
- `/health` works

---

### Issue 13: Deploy to GCP Cloud Run

**Goal**

Deploy the API to Cloud Run.

**Tasks**

- Create Artifact Registry repository
- Build container image
- Push image
- Deploy Cloud Run service
- Connect to Cloud SQL PostgreSQL
- Configure environment variables
- Configure service account
- Enable Vertex AI permissions

**Acceptance Criteria**

- Cloud Run URL is available
- `/health` works
- API can connect to Cloud SQL
- API can call Vertex AI when enabled

---

## 11. Codex Usage

Codex should use `AGENTS.md` as its primary build guide.

### Start Codex

From repo root:

```bash
codex
```

Or:

```bash
codex "Read AGENTS.md and implement the next milestone."
```

---

## 12. Codex Prompts by Milestone

### Milestone 1: PostgreSQL Ontology Store

```text
Read AGENTS.md and implement the PostgreSQL ontology store.

Implement:
1. SQLAlchemy session handling in app/db/connection.py
2. app/ontology/repository.py with object and relationship persistence
3. app/db/seed_ontology.py improvements
4. Tests for repository behavior
5. README updates

Keep the implementation simple and do not add Neo4j or Kafka.
```

---

### Milestone 2: Parsers

```text
Read AGENTS.md and implement the parser modules.

Implement:
1. COBOL parser:
   - PROGRAM-ID
   - CALL statements
   - COPY statements
   - EXEC SQL
   - file references
   - chunks with line numbers

2. JCL parser:
   - job name
   - steps
   - EXEC PGM
   - DD datasets

3. Copybook parser:
   - 01-level records
   - field names
   - PIC clauses

Add tests using files under data/samples.
```

---

### Milestone 3: Ingestion Pipeline

```text
Read AGENTS.md and implement the ingestion pipeline.

The pipeline should:
1. Walk a directory recursively
2. Classify files as COBOL, JCL, copybook, or documentation
3. Parse files
4. Store source artifacts
5. Store artifact chunks
6. Store ontology objects
7. Store ontology relationships
8. Store chunks in ChromaDB

Update /ingest/path to call the real pipeline.
Add tests.
```

---

### Milestone 4: Graph and Impact Analysis

```text
Read AGENTS.md and implement the graph and impact analysis layer.

Implement:
1. graph_loader.py to load PostgreSQL ontology into NetworkX
2. impact_analyzer.py with:
   - upstream
   - downstream
   - shortest paths
   - impact analysis
   - high-risk nodes
3. API endpoints for impact analysis
4. Tests
```

---

### Milestone 5: Agent Tools

```text
Read AGENTS.md and implement agent tools.

Implement:
1. get_program_summary
2. get_program_dependencies
3. get_program_business_rules
4. get_job_flow
5. get_impacted_assets
6. search_source_evidence
7. get_modernization_candidates
8. generate_impact_assessment

The tools should use PostgreSQL, ChromaDB, and NetworkX.
Do not allow arbitrary SQL execution.
```

---

### Milestone 6: Agent Ask Endpoint

```text
Read AGENTS.md and implement /agent/ask.

The endpoint should:
1. Classify question intent
2. Retrieve ontology facts
3. Retrieve source evidence from vector search
4. Run graph traversal if needed
5. Use mock LLM provider to synthesize answer
6. Return answer with evidence references

Add tests for sample questions.
```

---

### Milestone 7: Vertex AI Integration

```text
Read AGENTS.md and implement Vertex AI provider abstractions.

Implement:
1. BaseLLMProvider
2. MockLLMProvider
3. VertexAIGeminiProvider
4. BaseEmbeddingProvider
5. MockEmbeddingProvider
6. VertexAIEmbeddingProvider

Tests must use mock providers and should not require GCP credentials.
```

---

### Milestone 8: Docker and Cloud Run

```text
Read AGENTS.md and add deployment support.

Implement:
1. Dockerfile
2. docker-compose.yml for local PostgreSQL
3. Cloud Run deployment guide
4. Environment variable documentation
5. Health check validation
6. Optional GitHub Actions workflow for tests
```

---

## 13. GCP Deployment Plan

### 13.1 GCP services

Use:

- Cloud SQL for PostgreSQL
- Cloud Run for FastAPI
- Artifact Registry for container image
- Secret Manager for secrets
- Vertex AI for Gemini
- Vertex AI Search for enterprise-scale document search, if enabled
- Cloud Build or GitHub Actions for CI/CD

---

### 13.2 Enable APIs

```bash
gcloud services enable run.googleapis.com
gcloud services enable sqladmin.googleapis.com
gcloud services enable artifactregistry.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable secretmanager.googleapis.com
gcloud services enable aiplatform.googleapis.com
```

---

### 13.3 Create Artifact Registry

```bash
gcloud artifacts repositories create mainframe-intelligence \
  --repository-format=docker \
  --location=us-central1 \
  --description="Mainframe Intelligence API images"
```

---

### 13.4 Create Cloud SQL PostgreSQL

```bash
gcloud sql instances create mainframe-intelligence-db \
  --database-version=POSTGRES_16 \
  --cpu=2 \
  --memory=8GB \
  --region=us-central1
```

Create database:

```bash
gcloud sql databases create mainframe_intelligence \
  --instance=mainframe-intelligence-db
```

Create user:

```bash
gcloud sql users create app_user \
  --instance=mainframe-intelligence-db \
  --password=<strong-password>
```

---

### 13.5 Store secrets

```bash
echo -n "postgresql+psycopg2://app_user:<password>@/<db-name>?host=/cloudsql/<connection-name>" | \
gcloud secrets create mainframe-database-url --data-file=-
```

---

### 13.6 Build container image

```bash
gcloud builds submit \
  --tag us-central1-docker.pkg.dev/<PROJECT_ID>/mainframe-intelligence/api:latest
```

---

### 13.7 Deploy to Cloud Run

```bash
gcloud run deploy mainframe-intelligence-api \
  --image us-central1-docker.pkg.dev/<PROJECT_ID>/mainframe-intelligence/api:latest \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated \
  --add-cloudsql-instances <PROJECT_ID>:us-central1:mainframe-intelligence-db \
  --set-secrets DATABASE_URL=mainframe-database-url:latest \
  --set-env-vars APP_ENV=prod,GOOGLE_CLOUD_PROJECT=<PROJECT_ID>,GOOGLE_CLOUD_LOCATION=us-central1
```

---

### 13.8 Grant Vertex AI permission

Identify the Cloud Run service account and grant:

```bash
gcloud projects add-iam-policy-binding <PROJECT_ID> \
  --member="serviceAccount:<SERVICE_ACCOUNT_EMAIL>" \
  --role="roles/aiplatform.user"
```

---

## 14. GitHub Actions CI

Create:

```text
.github/workflows/ci.yml
```

Suggested workflow:

```yaml
name: CI

on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main, develop]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: pytest
```

---

## 15. Minimum Viable Product Definition

The MVP is complete when the team can:

1. Ingest sample COBOL, JCL, and copybook files
2. Store parsed assets in PostgreSQL
3. Store relationships such as:
   - `JCLJob EXECUTES Program`
   - `Program CALLS Program`
   - `Program USES_COPYBOOK Copybook`
   - `Copybook DEFINES DataElement`
4. Store searchable chunks in ChromaDB
5. Load dependency graph into NetworkX
6. Run impact analysis
7. Ask natural language questions using `/agent/ask`
8. Return answers with evidence references
9. Deploy the API to Cloud Run

---

## 16. Demo Script

Use this for the first demo.

### Step 1: Ingest sample data

```bash
curl -X POST http://localhost:8000/ingest/path \
  -H "Content-Type: application/json" \
  -d "{\"path\":\"data/samples\"}"
```

### Step 2: Ask for program summary

```bash
curl http://localhost:8000/program/SETL001/summary
```

### Step 3: Ask for dependencies

```bash
curl http://localhost:8000/program/SETL001/dependencies
```

### Step 4: Ask for job flow

```bash
curl http://localhost:8000/job/EODSETL/flow
```

### Step 5: Ask for impact analysis

```bash
curl http://localhost:8000/impact/program/SETL001
```

### Step 6: Ask the agent

```bash
curl -X POST http://localhost:8000/agent/ask \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"What is impacted if SETL001 changes?\"}"
```

---

## 17. Team Roles

Recommended initial team:

| Role | Responsibility |
|---|---|
| Product Owner / Architect | Defines ontology, business capabilities, modernization use cases |
| Python Backend Engineer | FastAPI, repository, ingestion, APIs |
| Mainframe SME | COBOL/JCL/copybook validation |
| Data Engineer | PostgreSQL schema, ChromaDB, Vertex AI Search |
| AI Engineer | Gemini prompts, extraction, agent orchestration |
| DevOps Engineer | Docker, Cloud Run, Cloud SQL, CI/CD |
| QA Engineer | Parser tests, API tests, regression data |

---

## 18. Engineering Principles

Use these principles throughout the build:

1. **Do not make the LLM the database**
   - Store durable knowledge in PostgreSQL and vector stores.

2. **Every answer needs evidence**
   - Artifact name, line range, relationship path, or source object.

3. **Start with deterministic parsing**
   - Use Gemini to enrich and explain, not as the only parser.

4. **Keep the ontology simple first**
   - Program, Job, Copybook, DataElement, BusinessRule, BusinessCapability.

5. **Expose tools, not raw SQL**
   - Agents should call safe API tools.

6. **Design for auditability**
   - Store confidence score, evidence URI, timestamps, and metadata.

7. **Modernization should be business-aware**
   - Do not just translate COBOL to Java.
   - First understand business capability, rules, data, dependencies, and tests.

---

## 19. Recommended First Sprint

### Sprint Goal

Build the first working ontology-backed ingestion flow.

### Sprint Scope

- PostgreSQL repository
- COBOL parser
- JCL parser
- Copybook parser
- Ingestion pipeline
- Basic dependency endpoint
- Basic impact endpoint
- Tests

### Sprint Demo

Show:

```text
SETL001.cbl + EODSETL.jcl + TRADE-REC.cpy
        |
        v
Ingestion
        |
        v
PostgreSQL ontology
        |
        v
NetworkX graph
        |
        v
API response:
"What is impacted if SETL001 changes?"
```

---

## 20. Commit Checklist

Before every PR:

```bash
pytest
```

Check:

- No credentials committed
- `.env` is not committed
- Tests pass
- README updated if setup changed
- API contracts documented
- Parser behavior tested
- Evidence metadata preserved

Commit:

```bash
git add .
git commit -m "<clear message>"
git push
```

---

## 21. Immediate Next Commands

From local repo:

```bash
git checkout -b develop
git push -u origin develop
```

Create the guide:

```bash
git add TEAM_BUILD_AND_DEPLOYMENT_GUIDE.md
git commit -m "Add team build and deployment guide"
git push
```

Create first feature branch:

```bash
git checkout -b feature/postgres-ontology-repository
```

Then ask Codex:

```text
Read AGENTS.md and TEAM_BUILD_AND_DEPLOYMENT_GUIDE.md. Implement Issue 1: PostgreSQL Ontology Repository.
```
