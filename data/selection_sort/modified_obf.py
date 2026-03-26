def a(basd):
    sdfg = len(basd)
    for asd in range(sdfg):
        asdfgf= asd
        for jasd in range(asd + 1, sdfg):
            if basd[jasd] < basd[asdfgf]:
                asdfgf = jasd
        if asdfgf != asd:
            basd[asd], basd[asdfgf] = basd[asdfgf], basd[asd]
    return basd