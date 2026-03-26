def busqueda_binaria(lista_ordenada, valor_objetivo):
    """
    Busca por el valor_objetivo en la lista_ordenada usand busqueda binaria.
    Retorna el indice de valor_objetivo si es encontrado, o -1 si no esta presente.
    """
    indice_izquierdo = 0
    indice_derecho = len(lista_ordenada) - 1

    while indice_izquierdo <= indice_derecho:
        indice_medio = (indice_izquierdo + indice_derecho) // 2
        valor_medio = lista_ordenada[indice_medio]

        if valor_medio == valor_objetivo:
            return indice_medio
        elif valor_medio < valor_objetivo:
            indice_izquierdo = indice_medio + 1
        else:
            indice_derecho = indice_medio - 1

    return -1