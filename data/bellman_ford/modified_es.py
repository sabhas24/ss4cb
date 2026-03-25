class Grafo:
    def __init__(self, tamanio):
        # Usar "None" para "sin arista" para que el peso 0 siga siendo válido.
        self.matriz_ady = [[None] * tamanio for _ in range(tamanio)]
        self.tamanio = tamanio
        self.datos_vertice = [""] * tamanio

    def agregar_arista(self, u, v, peso):
        if 0 <= u < self.tamanio and 0 <= v < self.tamanio:
            self.matriz_ady[u][v] = peso
            # self.matriz_ady[v][u] = peso  # Para grafos no dirigidos

    def agregar_datos_vertice(self, vertice, datos):
        if 0 <= vertice < self.tamanio:
            self.datos_vertice[vertice] = datos

    def bellman_ford(self, inicio_datos_vertice):
        if inicio_datos_vertice not in self.datos_vertice:
            raise ValueError(
                f"Vertice de inicio '{inicio_datos_vertice}' no encontrado"
            )

        vertice_inicio = self.datos_vertice.index(inicio_datos_vertice)
        distancias = [float("inf")] * self.tamanio
        predecesores = [None] * self.tamanio
        distancias[vertice_inicio] = 0

        for i in range(self.tamanio - 1):
            for u in range(self.tamanio):
                for v in range(self.tamanio):
                    peso = self.matriz_ady[u][v]
                    if peso is not None and distancias[u] != float("inf"):
                        if distancias[u] + peso < distancias[v]:
                            distancias[v] = distancias[u] + peso
                            predecesores[v] = u
                            print(
                                f"Relajar arista {self.datos_vertice[u]}->{self.datos_vertice[v]}, Distancia actualizada a {self.datos_vertice[v]}: {distancias[v]}"
                            )

        # Detección de ciclo negativo
        for u in range(self.tamanio):
            for v in range(self.tamanio):
                peso = self.matriz_ady[u][v]
                if peso is not None and distancias[u] != float("inf"):
                    if distancias[u] + peso < distancias[v]:
                        return (
                            True,
                            None,
                            None,
                        )  # Indicar que se encontró un ciclo negativo

        return (
            False,
            distancias,
            predecesores,
        )  # Indicar que no se encontró un ciclo negativo y devolver las distancias

    def obtener_camino(self, predecesores, vertice_inicio, vertice_final):
        camino = []
        actual = self.datos_vertice.index(vertice_final)
        while actual is not None:
            camino.insert(0, self.datos_vertice[actual])
            actual = predecesores[actual]
            if actual == self.datos_vertice.index(vertice_inicio):
                camino.insert(0, vertice_inicio)
                break
        return "->".join(camino)
