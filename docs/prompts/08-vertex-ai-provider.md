@workspace Read AGENTS.md and TEAM_BUILD_AND_DEPLOYMENT_GUIDE.md.

Implement Vertex AI and mock provider abstractions.

Files:
- app/agents/llm.py
- app/vectorstore/embeddings.py
- app/config.py
- tests/

Implement:
- BaseLLMProvider
- MockLLMProvider
- VertexAIGeminiProvider placeholder or real implementation if dependency is already available
- BaseEmbeddingProvider
- MockEmbeddingProvider
- VertexAIEmbeddingProvider placeholder

Tests must use mock providers and should not require GCP credentials.