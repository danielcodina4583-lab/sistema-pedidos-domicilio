class Cliente:
    def __init__(self, codigo, nombre, zona):
        self.codigo = codigo
        self.nombre = nombre
        self.zona = zona
        self.historial_pedidos = []
    
    def __str__(self):
        return f"Cliente {self.codigo}: {self.nombre} (Zona: {self.zona})"