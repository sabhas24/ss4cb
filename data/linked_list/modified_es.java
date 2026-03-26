class ListaEnlazada {

    private static class NodoLista {
        int nodoValor;
        NodoLista nodoSiguiente;

        NodoLista(int nodoValor) {
            this.nodoValor = nodoValor;
            this.nodoSiguiente = null;
        }
    }

    private NodoLista nodoCabeza;

    /** Insertar un nuevo nodo con valor al final de la lista */
    public void insertarAlFinal(int nuevoValor) {
        NodoLista nuevoNodo = new NodoLista(nuevoValor);
        if (nodoCabeza == null) {
            nodoCabeza = nuevoNodo;
            return;
        }
        NodoLista nodoActual = nodoCabeza;
        while (nodoActual.nodoSiguiente != null) {
            nodoActual = nodoActual.nodoSiguiente;
        }
        nodoActual.nodoSiguiente = nuevoNodo;
    }

    /** Elimina el primer nodo encontrado con valorObjetivo dado */
    public void eliminarPorValor(int valorObjetivo) {
        if (nodoCabeza == null)
            return;
        if (nodoCabeza.nodoValor == valorObjetivo) {
            nodoCabeza = nodoCabeza.nodoSiguiente;
            return;
        }
        NodoLista nodoActual = nodoCabeza;
        while (nodoActual.nodoSiguiente != null) {
            if (nodoActual.nodoSiguiente.nodoValor == valorObjetivo) {
                nodoActual.nodoSiguiente = nodoActual.nodoSiguiente.nodoSiguiente;
                return;
            }
            nodoActual = nodoActual.nodoSiguiente;
        }
    }

    /** Imprimir el valor de todos los nodos de cabeza a cola */
    public void imprimirLista() {
        NodoLista nodoActual = nodoCabeza;
        while (nodoActual != null) {
            System.out.print(nodoActual.nodoValor + " -> ");
            nodoActual = nodoActual.nodoSiguiente;
        }
        System.out.println("null");
    }
}
