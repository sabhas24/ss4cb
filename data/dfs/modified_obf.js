function f(g, s) {
    const v = new Set();
    const r = [];
    function ex(c) {
        v.add(c); r.push(c);
        for (const n of (g[c] || []))
            if (!v.has(n)) ex(n);
    }
    ex(s);
    return r;
}
