def n_esimo_fibonacci(n: int) -> int:
    """
    Calcular el n-ésimo número de la secuencia de Fibonacci.

    La secuencia de Fibonacci se define como:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) para n >= 2

    Parámetros:
        n (int): La posición en la secuencia Fibonacci (Debe ser >= 0).

    Retorna:
        int: El n-ésimo número Fibonacci.

    Excepciones:
        ValueError: Si n es un entero negativo.
    """
    # Validar entrada
    if n < 0:
        raise ValueError("n debe ser un entero no negativo")

    # Manejar los casos base directamente
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Inicializar los primeros dos números Fibonacci
    previo, actual = 0, 1

    # Computar iterativamente el n-ésimo número
    for _ in range(2, n + 1):
        # Actualizar valores: siguiente = previo + actual
        previo, actual = actual, previo + actual

    return actual
