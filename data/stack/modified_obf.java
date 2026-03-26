class S {
    private int[] a;
    private int t;
    private int c;

    public S(int c) {
        this.c = c;
        this.a = new int[c];
        this.t = -1;
    }

    public boolean e() {
        return t == -1;
    }

    public boolean f() {
        return t == c - 1;
    }

    public void pu(int v) {
        if (f()) {
            System.out.println("overflow");
            return;
        }
        a[++t] = v;
    }

    public int po() {
        if (e()) {
            System.out.println("underflow");
            return -1;
        }
        return a[t--];
    }

    public int pk() {
        if (e()) {
            System.out.println("empty");
            return -1;
        }
        return a[t];
    }
}
