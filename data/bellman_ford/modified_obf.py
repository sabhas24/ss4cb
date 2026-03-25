class Grafo:
    def __init__(self, tm):
        # Usar "None" para "sin arista" para que el ps 0 siga siendo válido.
        self.ma = [[None] * tm for _ in range(tm)]
        self.tm = tm
        self.dv = [""] * tm

    def aa(self, u, v, ps):
        if 0 <= u < self.tm and 0 <= v < self.tm:
            self.ma[u][v] = ps

    def a_dv(self, vr, dt):
        if 0 <= vr < self.tm:
            self.dv[vr] = dt

    def bf(self, i_dv):
        if i_dv not in self.dv:
            raise ValueError(f"Vertice de inicio '{i_dv}' no encontrado")

        vr_i = self.dv.index(i_dv)
        dss = [float("inf")] * self.tm
        prs = [None] * self.tm
        dss[vr_i] = 0

        for i in range(self.tm - 1):
            for u in range(self.tm):
                for v in range(self.tm):
                    ps = self.ma[u][v]
                    if ps is not None and dss[u] != float("inf"):
                        if dss[u] + ps < dss[v]:
                            dss[v] = dss[u] + ps
                            prs[v] = u
                            print(
                                f"Relajar arista {self.dv[u]}->{self.dv[v]}, Distancia actualizada a {self.dv[v]}: {dss[v]}"
                            )

        # Detección de ciclo negativo
        for u in range(self.tm):
            for v in range(self.tm):
                ps = self.ma[u][v]
                if ps is not None and dss[u] != float("inf"):
                    if dss[u] + ps < dss[v]:
                        return (
                            True,
                            None,
                            None,
                        )  # Indicar que se encontró un ciclo negativo

        return (
            False,
            dss,
            prs,
        )  # Indicar que no se encontró un ciclo negativo y devolver las dss

    def ooc(self, prs, vr_i, vrfvf):
        ccmm = []
        actttv = self.dv.index(vrfvf)
        while actttv is not None:
            ccmm.insert(0, self.dv[actttv])
            actttv = prs[actttv]
            if actttv == self.dv.index(vr_i):
                ccmm.insert(0, vr_i)
                break
        return "->".join(ccmm)
