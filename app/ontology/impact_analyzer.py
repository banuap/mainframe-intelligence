"""Impact analysis placeholder."""

import networkx as nx


def downstream(graph: nx.DiGraph, node: str, depth: int = 3) -> list[str]:
    """Return downstream impacted nodes up to a depth. Placeholder implementation."""
    if node not in graph:
        return []
    visited: set[str] = set()
    frontier = {node}
    for _ in range(depth):
        next_frontier: set[str] = set()
        for current in frontier:
            next_frontier.update(graph.successors(current))
        next_frontier -= visited
        visited.update(next_frontier)
        frontier = next_frontier
    return sorted(visited)
