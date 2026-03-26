class LL {
    private static class N {
        int v;
        N nx;

        N(int v) {
            this.v = v;
            this.nx = null;
        }
    }

    private N h;

    public void ins(int v) {
        N nd = new N(v);
        if (h == null) {
            h = nd;
            return;
        }
        N c = h;
        while (c.nx != null)
            c = c.nx;
        c.nx = nd;
    }

    public void del(int v) {
        if (h == null)
            return;
        if (h.v == v) {
            h = h.nx;
            return;
        }
        N c = h;
        while (c.nx != null) {
            if (c.nx.v == v) {
                c.nx = c.nx.nx;
                return;
            }
            c = c.nx;
        }
    }

    public void pr() {
        N c = h;
        while (c != null) {
            System.out.print(c.v + " -> ");
            c = c.nx;
        }
        System.out.println("null");
    }

}
