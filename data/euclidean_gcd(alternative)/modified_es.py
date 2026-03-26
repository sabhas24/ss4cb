def mcd_euclideas(primero_numero, segundo_numero):
    """
    Retorna el mayor comun divisor del primer y segund numero
    usando el algoritmo euclideo
    """
    dividendo = primero_numero
    divisor = segundo_numero

    while divisor != 0:
        resto = dividendo % divisor
        dividendo = divisor
        divisor = resto

    return dividendo