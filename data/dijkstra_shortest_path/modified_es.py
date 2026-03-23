import heapq

def dijkstra(grafo, origen):
    """
    Calcula el camino más corto desde el origen hacia todos los demás nodos
    usando el algoritmo de Dijkstra con una cola de prioridad (min-heap).
    """
    num_nodos = len(grafo)
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0
    nodo_anterior = {nodo: None for nodo in grafo}
    cola_prioridad = [(0, origen)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso_arista in grafo[nodo_actual].items():
            nueva_distancia = distancia_actual + peso_arista

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                nodo_anterior[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

    return distancias, nodo_anterior


def reconstruir_camino(nodo_anterior, destino):
    """Reconstruye el camino más corto hasta el nodo destino."""
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = nodo_anterior[actual]
    return list(reversed(camino))
