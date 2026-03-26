def f(lst, t):
    l = 0
    r = len(lst) - 1
    while l <= r:
        m = (l + r) // 2
        if lst[m] == t:
            return m
        elif lst[m] < t:
            l = m + 1
        else:
            r = m - 1
    return -1
