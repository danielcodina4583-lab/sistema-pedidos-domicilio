class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.frente = None
        self.fin = None
        self.size = 0

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.frente is None:
            self.frente = self.fin = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.frente
            self.frente = nuevo_nodo
        self.size += 1

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.frente is None:
            self.frente = self.fin = nuevo_nodo
        else:
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo
        self.size += 1

    def buscar(self, criterio):
        tmp = self.frente
        while tmp is not None:
            if criterio(tmp.dato):
                return tmp.dato
            tmp = tmp.siguiente
        return None

    def buscar_todos(self, criterio):
        resultados = []
        tmp = self.frente
        while tmp is not None:
            if criterio(tmp.dato):
                resultados.append(tmp.dato)
            tmp = tmp.siguiente
        return resultados

    def recorrer(self):
        elementos = []
        tmp = self.frente
        while tmp is not None:
            elementos.append(str(tmp.dato))
            tmp = tmp.siguiente
        return elementos

    def esta_vacia(self):
        return self.frente is None

    def __iter__(self):
        actual = self.frente
        while actual:
            yield actual.dato
            actual = actual.siguiente