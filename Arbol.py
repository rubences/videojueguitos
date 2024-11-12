from NodoArbol import NodoArbol

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor):
        self.raiz = self._insertar_recursivo(self.raiz, clave, valor)

    def _insertar_recursivo(self, nodo_actual, clave, valor):
        if nodo_actual is None:
            return NodoArbol(clave, valor)
        if clave < nodo_actual.clave:
            nodo_actual.izquierda = self._insertar_recursivo(nodo_actual.izquierda, clave, valor)
        elif clave > nodo_actual.clave:
            nodo_actual.derecha = self._insertar_recursivo(nodo_actual.derecha, clave, valor)
        else:
            # Si la clave ya existe, actualizar el valor
            nodo_actual.valor = valor
        return nodo_actual

    def inorden(self):
        self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo_actual):
        if nodo_actual:
            self._inorden_recursivo(nodo_actual.izquierda)
            print(nodo_actual.valor)
            self._inorden_recursivo(nodo_actual.derecha)

    def por_nivel(self):
        if self.raiz is None:
            return
        cola = [self.raiz]
        while cola:
            nodo_actual = cola.pop(0)
            print(nodo_actual.valor)
            if nodo_actual.izquierda:
                cola.append(nodo_actual.izquierda)
            if nodo_actual.derecha:
                cola.append(nodo_actual.derecha)

    def buscar(self, clave):
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, nodo_actual, clave):
        if nodo_actual is None or nodo_actual.clave == clave:
            return nodo_actual
        if clave < nodo_actual.clave:
            return self._buscar_recursivo(nodo_actual.izquierda, clave)
        return self._buscar_recursivo(nodo_actual.derecha, clave)
    

