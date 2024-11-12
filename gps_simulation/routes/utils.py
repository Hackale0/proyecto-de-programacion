import heapq
from .models import Ciudad, Ruta

def dijkstra(ciudad_inicial):
    # Inicializa las distancias y la lista de predecesores
    distancias = {ciudad_inicial: 0}
    ciudades_anteriores = {ciudad_inicial: None}
    cola_prioridad = [(0, ciudad_inicial)]  # Cola de prioridad para almacenar las ciudades a procesar

    while cola_prioridad:
        # Extrae la ciudad con la menor distancia
        distancia_actual, ciudad_actual = heapq.heappop(cola_prioridad)

        # Obtiene las rutas que salen de la ciudad actual
        rutas = Ruta.objects.filter(ciudad_origen=ciudad_actual)

        for ruta in rutas:
            vecino = ruta.ciudad_destino
            peso = ruta.distancia
            distancia = distancia_actual + peso

            # Si se encuentra una ruta más corta hacia el vecino, se actualizan las estructuras
            if vecino not in distancias or distancia < distancias[vecino]:
                distancias[vecino] = distancia
                ciudades_anteriores[vecino] = ciudad_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias, ciudades_anteriores


class ArbolBinarioBusqueda:

    def __init__(self):
        # Inicializa el árbol binario de búsqueda.
        # 'raiz' se establece como None, lo que significa que el árbol está vacío inicialmente.
        # 'tamano' se inicializa en 0 para rastrear cuántos nodos tiene el árbol.
        self.raiz = None
        self.tamano = 0

    def agregar(self, clave, valor):
        # Método para agregar un nuevo nodo al árbol.
        # Si el árbol ya tiene una raíz, llama a _agregar() para ubicar el nuevo nodo correctamente.
        # Si no hay raíz, el nuevo nodo se convierte en la raíz del árbol.
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
        # Incrementa el tamaño del árbol cada vez que se agrega un nuevo nodo.
        self.tamano = self.tamano + 1

    def _agregar(self, clave, valor, nodoActual):
        # Método auxiliar recursivo para ubicar correctamente el nuevo nodo en el árbol.
        # Si la clave es menor que la clave del nodo actual, busca en el subárbol izquierdo.
        if clave < nodoActual.clave:
            # Si el nodo actual tiene un hijo izquierdo, continúa la recursión.
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave, valor, nodoActual.hijoIzquierdo)
            else:
                # Si no tiene hijo izquierdo, crea un nuevo nodo allí.
                nodoActual.hijoIzquierdo = NodoArbol(clave, valor, padre=nodoActual)
        else:
            # Si la clave es mayor o igual a la clave del nodo actual, busca en el subárbol derecho.
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave, valor, nodoActual.hijoDerecho)
            else:
                # Si no tiene hijo derecho, crea un nuevo nodo allí.
                nodoActual.hijoDerecho = NodoArbol(clave, valor, padre=nodoActual)

    def __setitem__(self, c, v):
        # Sobrecarga del operador [] para agregar elementos al árbol.
        # Permite hacer algo como: arbol[clave] = valor
        self.agregar(c, v)

    def obtener(self, clave):
        # Método para obtener el valor asociado a una clave dada.
        # Si el árbol tiene una raíz, busca la clave llamando al método auxiliar _obtener().
        if self.raiz:
            res = self._obtener(clave, self.raiz)
            if res:
                # Si encuentra el nodo, devuelve el valor (carga útil) del nodo.
                return res.cargaUtil
            else:
                # Si no se encuentra la clave, devuelve None.
                return None
        else:
            return None

    def _obtener(self, clave, nodoActual):
        # Método auxiliar recursivo para encontrar el nodo con la clave especificada.
        if not nodoActual:
            # Si el nodo actual es None, significa que la clave no está en el árbol.
            return None
        elif nodoActual.clave == clave:
            # Si la clave del nodo actual coincide con la clave buscada, devuelve el nodo.
            return nodoActual
        elif clave < nodoActual.clave:
            # Si la clave buscada es menor, busca en el subárbol izquierdo.
            return self._obtener(clave, nodoActual.hijoIzquierdo)
        else:
            # Si la clave buscada es mayor, busca en el subárbol derecho.
            return self._obtener(clave, nodoActual.hijoDerecho)

    def obtener_claves(self):
        claves = []
        self._obtener_claves(self.raiz, claves)
        return claves

    def _obtener_claves(self, nodoActual, claves):
        if nodoActual:
            self._obtener_claves(nodoActual.hijoIzquierdo, claves)  # Recorrer el hijo izquierdo
            claves.append(nodoActual.clave)  # Añadir la clave del nodo actual
            self._obtener_claves(nodoActual.hijoDerecho, claves)  # Recorrer el hijo derecho

    def obtener_lista(self):
        return [self.obtener(clave) for clave in self.obtener_claves()]

    def __getitem__(self,clave):
        res = self.obtener(clave)
        if res:
            return res
        else:
            raise KeyError('Error, la clave no está en el árbol')

    def __contains__(self,clave):
        if self._obtener(clave,self.raiz):
            return True
        else:
            return False

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def __iter__(self):
        return self.raiz.__iter__()

    def eliminar(self,clave):
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave,self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano-1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')

    def __delitem__(self,clave):
        self.eliminar(clave)

    def remover(self,nodoActual):
        if nodoActual.esHoja(): #hoja
            if nodoActual == nodoActual.padre.hijoIzquierdo:
                nodoActual.padre.hijoIzquierdo = None
            else:
                nodoActual.padre.hijoDerecho = None
        elif nodoActual.tieneAmbosHijos(): #interior
            suc = nodoActual.encontrarSucesor()
            suc.empalmar()
            nodoActual.clave = suc.clave
            nodoActual.cargaUtil = suc.cargaUtil

        else: # este nodo tiene un (1) hijo
            if nodoActual.tieneHijoIzquierdo():
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave, nodoActual.hijoIzquierdo.cargaUtil, nodoActual.hijoIzquierdo.hijoIzquierdo, nodoActual.hijoIzquierdo.hijoDerecho)
            else:
                if nodoActual.esHijoIzquierdo():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                elif nodoActual.esHijoDerecho():
                    nodoActual.hijoDerecho.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave, nodoActual.hijoDerecho.cargaUtil, nodoActual.hijoDerecho.hijoIzquierdo, nodoActual.hijoDerecho.hijoDerecho)

    def inorden(self):
        self._inorden(self.raiz)

    def _inorden(self,arbol):
        if arbol != None:
            self._inorden(arbol.hijoIzquierdo)
            print(arbol.clave)
            self._inorden(arbol.hijoDerecho)

    def postorden(self):
        self._postorden(self.raiz)

    def _postorden(self, arbol):
        if arbol:
            self._postorden(arbol.hijoDerecho)
            self._postorden(arbol.hijoIzquierdo)
            print(arbol.clave)

    def preorden(self):
        self._preorden(self.raiz)

    def _preorden(self,arbol):
        if arbol:
            print(arbol.clave)
            self._preorden(arbol.hijoIzquierdo)
            self._preorden(arbol.hijoDerecho)

class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

    def encontrarSucesor(self):
        suc = None
        if self.tieneHijoDerecho():
            suc = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
                if self.esHijoIzquierdo():
                    suc = self.padre
                else:
                    self.padre.hijoDerecho = None
                    suc = self.padre.encontrarSucesor()
                    self.padre.hijoDerecho = self
        return suc

    def empalmar(self):
        if self.esHoja():
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                self.hijoDerecho.padre = self.padre

    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def __iter__(self):
        if self:
            if self.tieneHijoIzquierdo():
                for elem in self.hijoIzquierdo:
                    yield elem
            yield self.clave
            if self.tieneHijoDerecho():
                for elem in self.hijoDerecho:
                    yield elem