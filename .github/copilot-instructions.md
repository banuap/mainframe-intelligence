\# GitHub Copilot Instructions



This project builds a Mainframe Application Intelligence Platform.



Follow these rules:



\- Use Python, FastAPI, PostgreSQL, SQLAlchemy, NetworkX, ChromaDB, and Vertex AI provider abstractions.

\- Do not add Neo4j, Kafka, TigerGraph, or new cloud services unless explicitly requested.

\- Do not hardcode credentials.

\- Keep LLM and embedding providers behind interfaces.

\- Agents must use safe tools and must not execute arbitrary SQL.

\- Every response should preserve evidence references where possible.

\- Use type hints and Pydantic models.

\- Add or update tests for every implementation.

\- Run `pytest` before completing changes.

