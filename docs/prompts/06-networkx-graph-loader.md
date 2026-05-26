@workspace Read AGENTS.md and TEAM_BUILD_AND_DEPLOYMENT_GUIDE.md.

Implement Issue 6: NetworkX Graph Loader.

Files:
- app/ontology/graph_loader.py
- app/ontology/impact_analyzer.py
- tests/test_impact_analysis.py

Implement:
- load graph from ontology objects and relationships
- node metadata
- edge metadata
- get_upstream
- get_downstream
- get_dependency_paths
- high_risk_nodes based on degree centrality

Add tests.