class Graph:
    def __init__(self, size):
        # Use None for "no edge" so weight 0 is still valid.
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [""] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            # self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def bellman_ford(self, start_vertex_data):
        if start_vertex_data not in self.vertex_data:
            raise ValueError(f"Start vertex '{start_vertex_data}' not found")

        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float("inf")] * self.size
        predecessors = [None] * self.size
        distances[start_vertex] = 0

        for i in range(self.size - 1):
            for u in range(self.size):
                for v in range(self.size):
                    weight = self.adj_matrix[u][v]
                    if weight is not None and distances[u] != float("inf"):
                        if distances[u] + weight < distances[v]:
                            distances[v] = distances[u] + weight
                            predecessors[v] = u
                            print(
                                f"Relaxing edge {self.vertex_data[u]}->{self.vertex_data[v]}, Updated distance to {self.vertex_data[v]}: {distances[v]}"
                            )

        # Negative cycle detection
        for u in range(self.size):
            for v in range(self.size):
                weight = self.adj_matrix[u][v]
                if weight is not None and distances[u] != float("inf"):
                    if distances[u] + weight < distances[v]:
                        return (True, None, None)  # Indicate a negative cycle was found

        return (
            False,
            distances,
            predecessors,
        )  # Indicate no negative cycle and return distances

    def get_path(self, predecessors, start_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessors[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
                break
        return "->".join(path)
