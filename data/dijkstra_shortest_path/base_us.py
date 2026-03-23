import heapq

def dijkstra(graph, source):
    """
    Computes the shortest path from source to all other nodes
    using Dijkstra's algorithm with a min-heap priority queue.
    """
    num_nodes = len(graph)
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    previous_node = {node: None for node in graph}
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, edge_weight in graph[current_node].items():
            new_distance = current_distance + edge_weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_node[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances, previous_node


def reconstruct_path(previous_node, target):
    """Reconstructs the shortest path to the target node."""
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous_node[current]
    return list(reversed(path))
