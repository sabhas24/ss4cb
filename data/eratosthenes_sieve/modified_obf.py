def f(n):
    a = [True] * (n + 1)
    a[0] = False
    a[1] = False
    i = 2
    while i * i <= n:
        if a[i]:
            j = i * i
            while j <= n:
                a[j] = False
                j += i
        i += 1
    return [x for x in range(2, n + 1) if a[x]]