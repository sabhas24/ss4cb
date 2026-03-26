def ordenamiento_por_seleccion(lista):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento por selección.
    
    Principios : 
    En cada iteración, se busca el elemento más pequeño de la parte 
    no ordenada de la lista, luego se intercambia con el elemento actual.
    
    lista: List de elementos a ordenar
    return: List ordenada (ordenamiento in situ)

    Complejidad :
    - Tiempo : O(n^2)
    - Espacio : O(1) (ordenamiento in situ)
    """
    n = len(lista)

    # Recorrido de toda la lista
    for i in range(n):
        # Suponemos que el mínimo es el primer elemento de la zona no ordenada
        indice_minimo = i

        # Búsqueda del elemento más pequeño en el resto de la lista
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        # Intercambio si se encontró un elemento más pequeño
        if indice_minimo != i:
            lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

    return lista
