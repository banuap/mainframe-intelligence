"""Impact analysis tests."""

import networkx as nx

from app.ontology.impact_analyzer import downstream


def test_downstream_empty_graph():
    graph = nx.DiGraph()
    assert downstream(graph, "SETL001") == []


def test_downstream_depth():
    graph = nx.DiGraph()
    graph.add_edge("SETL001", "ACCTUPD")
    graph.add_edge("ACCTUPD", "ACCOUNT_TABLE")
    assert downstream(graph, "SETL001", depth=1) == ["ACCTUPD"]
    assert downstream(graph, "SETL001", depth=2) == ["ACCOUNT_TABLE", "ACCTUPD"]
