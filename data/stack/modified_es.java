class Pila {
    private int[] arregloDeElementos;
    private int indiceSuperior;
    private int capacidadPila;

    /** Inicializa una pila con la capacidad dada */
    public Pila(int capacidadPila) {
        this.capacidadPila = capacidadPila;
        this.arregloDeElementos = new int[capacidadPila];
        this.indiceSuperior = -1;
    }

    /** Retorna verdadero si la pila no tiene elementos */
    public boolean estaVacia() {
        return indiceSuperior == -1;
    }

    /** Retorna verdadero si la pila alcanzo su capacidad */
    public boolean EstaLlena() {
        return indiceSuperior == capacidadPila - 1;
    }

    /** Agrega un nuevo elemento en la parte superior de la pila */
    public void insertar(int nuevoElemento) {
        if (EstaLlena()) {
            System.out.println("Desbordamiento de pila: No se puede insertar " + nuevoElemento);
            return;
        }
        arregloDeElementos[++indiceSuperior] = nuevoElemento;
    }

    /** Remueve y retorna el elemento superior de la pila */
    public int extraer() {
        if (estaVacia()) {
            System.out.println("Subdesbordamiento de pila: La pila esta vacia");
            return -1;
        }
        return arregloDeElementos[indiceSuperior--];
    }

    /** Retorna el elemento superior sin removerlo */
    public int ver() {
        if (estaVacia()) {
            System.out.println("La pila esta vacia");
            return -1;
        }
        return arregloDeElementos[indiceSuperior];
    }

}
