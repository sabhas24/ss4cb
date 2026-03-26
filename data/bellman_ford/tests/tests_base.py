import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from base_us import Graph


def build_sample_graph():
    g = Graph(5)

    g.add_vertex_data(0, "A")
    g.add_vertex_data(1, "B")
    g.add_vertex_data(2, "C")
    g.add_vertex_data(3, "D")
    g.add_vertex_data(4, "E")

    g.add_edge(3, 0, 4)  # D -> A, weight 4
    g.add_edge(3, 2, 7)  # D -> C, weight 7
    g.add_edge(3, 4, 3)  # D -> E, weight 3
    g.add_edge(0, 2, 4)  # A -> C, weight 4
    g.add_edge(2, 0, -3)  # C -> A, weight -3
    g.add_edge(0, 4, 5)  # A -> E, weight 5
    g.add_edge(4, 2, 3)  # E -> C, weight 3
    g.add_edge(1, 2, -4)  # B -> C, weight -4
    g.add_edge(4, 1, 2)  # E -> B, weight 2

    return g


def test_bellman_ford_sample_graph_from_d():
    g = build_sample_graph()

    negative_cycle, distances, predecessors = g.bellman_ford("D")

    assert negative_cycle is False
    assert distances == [-2, 5, 1, 0, 3]
    assert g.get_path(predecessors, "D", "C") == "D->E->B->C"


def test_bellman_ford_detects_negative_cycle():
    g = Graph(3)
    g.add_vertex_data(0, "A")
    g.add_vertex_data(1, "B")
    g.add_vertex_data(2, "C")

    # Cycle A -> B -> C -> A has total weight -1.
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, -1)
    g.add_edge(2, 0, -1)

    negative_cycle, distances, predecessors = g.bellman_ford("A")

    assert negative_cycle is True
    assert distances is None
    assert predecessors is None


def test_bellman_ford_raises_for_unknown_start_vertex():
    g = Graph(1)
    g.add_vertex_data(0, "A")

    with pytest.raises(ValueError, match="Start vertex 'Z' not found"):
        g.bellman_ford("Z")
