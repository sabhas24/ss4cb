# Dijkstra's Shortest Path

## Author
Joaquín Bogado (2026-03-23)

## Algorithm Description
Dijkstra's algorithm finds the shortest paths from a source node to all other
nodes in a weighted graph with non-negative edge weights. It maintains a
priority queue (min-heap) of nodes ordered by their current known distance
from the source. At each step, the node with the smallest distance is
extracted and its neighbors are relaxed: if a shorter path to a neighbor is
found through the current node, the neighbor's distance is updated. The
algorithm also records, for each node, which node preceded it on the shortest
path, allowing path reconstruction.

## Model Used to Create the Base Code
claude-sonnet-4-6

### Prompt
```
Write a Python implementation of Dijkstra's shortest path algorithm.
The function dijkstra(graph, source) should accept a graph as a dict of dicts
(adjacency list with edge weights) and a source node, and return a tuple of
(distances, previous_node) dicts. Also write a reconstruct_path(previous_node, target)
helper. Use a min-heap priority queue. Add docstrings and inline comments in English.
```

## Obfuscated Version
none
