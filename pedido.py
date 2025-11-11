from datetime import datetime

class Pedido:
    def __init__(self, codigo, cliente, restaurante, productos):
        self.codigo = codigo
        self.cliente = cliente
        self.restaurante = restaurante
        self.domiciliario = None
        self.productos = productos
        self.estado = "PENDIENTE"
        self.fecha_creacion = datetime.now()
        self.fecha_asignacion = None
        self.fecha_entrega = None
        self.distancia_total = 0

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        if nuevo_estado == "ASIGNADO":
            self.fecha_asignacion = datetime.now()
        elif nuevo_estado == "ENTREGADO":
            self.fecha_entrega = datetime.now()

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            encontrado = False
            for categoria in self.restaurante.menu.values():
                for item in categoria:
                    if item['nombre'] == producto:
                        total += item['precio']
                        encontrado = True
                        break
                if encontrado:
                    break
        return total

    def __str__(self):
        return f"Pedido {self.codigo}: {self.estado} | Cliente: {self.cliente.nombre} | Total: ${self.calcular_total()}"

    def detalle(self):
        if self.domiciliario:
            nombre_domiciliario = self.domiciliario.nombre
        else:
            nombre_domiciliario = 'No asignado'
            
        if self.fecha_entrega:
            fecha_entrega_texto = self.fecha_entrega.strftime('%Y-%m-%d %H:%M')
        else:
            fecha_entrega_texto = 'No entregado'
        
        info = "DETALLE PEDIDO " + self.codigo + "\n"
        info += "Estado: " + self.estado + "\n"
        info += "Cliente: " + self.cliente.nombre + " (Zona: " + self.cliente.zona + ")\n"
        info += "Restaurante: " + self.restaurante.nombre + " (Zona: " + self.restaurante.zona + ")\n"
        info += "Domiciliario: " + nombre_domiciliario + "\n"
        info += "Productos: " + ", ".join(self.productos) + "\n"
        info += "Total: $" + str(self.calcular_total()) + "\n"
        info += "Distancia: " + str(self.distancia_total) + "km\n"
        info += "Fecha creacion: " + self.fecha_creacion.strftime('%Y-%m-%d %H:%M') + "\n"
        info += "Fecha entrega: " + fecha_entrega_texto
        
        return info