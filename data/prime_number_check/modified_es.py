def es_primo(numero: int) -> bool:
    """
    Determina si un número dado es un número primo.

    Args:
        numero (int): El número a evaluar.

    Returns:
        bool: True si el número dado es primo, False en caso contrario.
    """

    # Los números primos son más grandes que 1
    if numero <= 1:
        return False

    # 2 es el único número primo par.
    if numero == 2:
        return True

    # Excluir todos los demás números pares mayores a 2
    if numero % 2 == 0:
        return False

    # Chequear la divisibilidad del número desde 3 hasta la raíz de número
    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2

    return True
