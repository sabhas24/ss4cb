def f(i: int) -> int:
    if i < 0:
        raise ValueError("iccanobiF")

    if i == 0:
        return 0
    if i == 1:
        return 1

    b, o = 0, 1

    for _ in range(2, i + 1):
        b, o = o, b + o

    return o
