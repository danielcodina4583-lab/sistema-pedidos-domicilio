class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila():
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.top
        self.top = nuevo_nodo
        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        dato = self.top.dato
        self.top = self.top.siguiente
        self.size -= 1
        return dato

    def tope(self):
        if self.top is None:
            return None
        return self.top.dato

    def esta_vacia(self):
        return self.top is None

    def mostrar(self):
        elementos = []
        tmp = self.top
        while tmp is not None:
            elementos.append(str(tmp.dato))
            tmp = tmp.siguiente
        return elementos