from NodoArbol import NodoArbol

class Arbol:
    def __init__(self):
        self.raiz = None

    def esta_vacio(self):
        return self.raiz is None
    
    def obtener(self, clave):
        nodo = self.buscar(clave)
        return nodo.valor if nodo else None
    
    def reemplazar(self, clave, valor):
        nodo = self.buscar(clave)
        if nodo:
            nodo.valor = valor
        else:
            raise KeyError("La clave no existe")
        
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

  
    def buscar(self, clave):
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, nodo_actual, clave):
        if nodo_actual is None or nodo_actual.clave == clave:
            return nodo_actual
        if clave < nodo_actual.clave:
            return self._buscar_recursivo(nodo_actual.izquierda, clave)
        return self._buscar_recursivo(nodo_actual.derecha, clave)
    
    def eliminar(self, clave):
        self.raiz = self._eliminar_recursivo(self.raiz, clave)

    def _eliminar_recursivo(self, nodo_actual, clave):
        if nodo_actual is None:
            return nodo_actual
        if clave < nodo_actual.clave:
            nodo_actual.izquierda = self._eliminar_recursivo(nodo_actual.izquierda, clave)
        elif clave > nodo_actual.clave:
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, clave)
        else:
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            if nodo_actual.derecha is None:
                return nodo_actual.izquierda
            nodo_actual.clave = self._minimo(nodo_actual.derecha)
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, nodo_actual.clave)
        return nodo_actual
    
    def modificar(self, clave, nuevo_clave, valor):
        self.modificar_recursivo(self.raiz, clave, nuevo_clave, valor)
        
    def modificar_recursivo(self, nodo_actual, clave, nuevo_clave, valor):
        if nodo_actual is None:
            raise KeyError("La clave no existe")
        if clave < nodo_actual.clave:
            self.modificar_recursivo(nodo_actual.izquierda, clave, nuevo_clave, valor)
        elif clave > nodo_actual.clave:
            self.modificar_recursivo(nodo_actual.derecha, clave, nuevo_clave, valor)
        else:
            nodo_actual.valor = valor
        
  
    def _maximo(self, nodo_actual):
        while nodo_actual.derecha:
            nodo_actual = nodo_actual.derecha
        return nodo_actual.clave
    
    
    def _minimo(self, nodo_actual):
        while nodo_actual.izquierda:
            nodo_actual = nodo_actual.izquierda
        return nodo_actual.clave
    

    def inorden(self):
        self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo_actual):
        if nodo_actual:
            self._inorden_recursivo(nodo_actual.izquierda)
            print(nodo_actual.valor)
            self._inorden_recursivo(nodo_actual.derecha)

    def preorden(self):
        self._preorden_recursivo(self.raiz)

    def _preorden_recursivo(self, nodo_actual):
        if nodo_actual:
            print(nodo_actual.valor)
            self._preorden_recursivo(nodo_actual.izquierda)
            self._preorden_recursivo(nodo_actual.derecha)

    def postorden(self):
        self._postorden_recursivo(self.raiz)

    def _postorden_recursivo(self, nodo_actual):
        if nodo_actual:
            self._postorden_recursivo(nodo_actual.izquierda)
            self._postorden_recursivo(nodo_actual.derecha)
            print(nodo_actual.valor)
    
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

    

