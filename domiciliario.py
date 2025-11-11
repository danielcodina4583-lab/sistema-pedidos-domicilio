class Domiciliario:
    def __init__(self, codigo, nombre, zona):
        self.codigo = codigo
        self.nombre = nombre
        self.zona = zona
        self.disponible = True
        self.pedido_actual = None
    
    def __str__(self):
        estado = " Disponible" if self.disponible else " Ocupado"
        return f"Domiciliario {self.codigo}: {self.nombre} - {estado} (Zona: {self.zona})"