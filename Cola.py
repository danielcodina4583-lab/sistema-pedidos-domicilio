class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.head is None:
            self.head = self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        dato = self.head.dato
        self.head = self.head.siguiente
        if self.head is None:
            self.tail = None
        self.size -= 1
        return dato

    def esta_vacia(self):
        return self.head is None

    def mostrar(self):
        elementos = []
        tmp = self.head
        while tmp is not None:
            elementos.append(str(tmp.dato))
            tmp = tmp.siguiente
        return elementos

    def frente(self):
        return self.head.dato if self.head else None

    def show(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.dato, end=" -> ")
            tmp = tmp.siguiente
        print("None")