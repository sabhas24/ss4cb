def criba_De_Eratostenes(limite):
    """
    Retorna una lista de todos los numeros primos hasta e incluyendo el limite
    usando el algoritmo de la Criba de Eratóstenes.
    """
    es_primo = [True] * (limite + 1)
    es_primo[0] = False
    es_primo[1] = False

    numero_actual = 2
    while numero_actual * numero_actual <= limite:
        if es_primo[numero_actual]:
            multiple = numero_actual * numero_actual
            while multiple <= limite:
                es_primo[multiple] = False
                multiple += numero_actual
        numero_actual += 1

    lista_primos = [numero for numero in range(2, limite + 1) if es_primo[numero]]
    return lista_primos