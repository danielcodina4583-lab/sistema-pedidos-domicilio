from Lista import Lista
from Cola import Cola
from Pila import Pila
from grafo import Grafo
from cliente import Cliente
from restaurante import Restaurante
from domiciliario import Domiciliario
from pedido import Pedido
from datetime import datetime
import time

class SistemaPedidos:
    def __init__(self):
        self.clientes = Lista()
        self.restaurantes = Lista()
        self.domiciliarios = Lista()
        self.pedidos_activos = Cola()
        self.pedidos_entregados = Pila()
        self.pedidos_cancelados = Pila()
        self.mapa = Grafo()
        self.contador_pedidos = 0

        self._inicializar_sistema()

    def _inicializar_sistema(self):
        # Barrios principales de Santa Marta
        barrios_santa_marta = [
            "Centro Historico", "Rodadero", "Bello Horizonte", 
            "Mamatoco", "Gaira", "Taganga", "Pozos Colorados"
        ]
        
        for barrio in barrios_santa_marta:
            self.mapa.agregar_zona(barrio)

      
        conexiones = [
            ("Centro Historico", "Rodadero", 5),
            ("Centro Historico", "Bello Horizonte", 3),
            ("Centro Historico", "Mamatoco", 2),
            ("Centro Historico", "Gaira", 6),
            ("Rodadero", "Pozos Colorados", 4),
            ("Rodadero", "Gaira", 8),
            ("Bello Horizonte", "Mamatoco", 4),
            ("Gaira", "Taganga", 12),
            ("Mamatoco", "Taganga", 10)
        ]

        for zona1, zona2, distancia in conexiones:
            self.mapa.conectar_zonas(zona1, zona2, distancia)

    def registrar_cliente(self, codigo, nombre, zona):
        if zona not in self.mapa.zonas:
            return "Zona '" + zona + "' no existe en el mapa"

        cliente_existente = self.clientes.buscar(lambda c: c.codigo == codigo)
        if cliente_existente:
            return "Ya existe un cliente con codigo " + codigo

        cliente = Cliente(codigo, nombre, zona)
        self.clientes.insertar_final(cliente)
        return "Cliente " + nombre + " registrado en zona " + zona

    def registrar_restaurante(self, codigo, nombre, zona):
        if zona not in self.mapa.zonas:
            return "Zona '" + zona + "' no existe en el mapa"

        restaurante_existente = self.restaurantes.buscar(lambda r: r.codigo == codigo)
        if restaurante_existente:
            return "Ya existe un restaurante con codigo " + codigo

        restaurante = Restaurante(codigo, nombre, zona)
        self.restaurantes.insertar_final(restaurante)
        return "Restaurante " + nombre + " registrado en zona " + zona

    def registrar_domiciliario(self, codigo, nombre, zona):
        if zona not in self.mapa.zonas:
            return "Zona '" + zona + "' no existe en el mapa"

        domiciliario_existente = self.domiciliarios.buscar(lambda d: d.codigo == codigo)
        if domiciliario_existente:
            return "Ya existe un domiciliario con codigo " + codigo

        domiciliario = Domiciliario(codigo, nombre, zona)
        self.domiciliarios.insertar_final(domiciliario)
        return "Domiciliario " + nombre + " registrado en zona " + zona

    def agregar_producto_restaurante(self, codigo_restaurante, nombre, precio, tipo):
        restaurante = self.restaurantes.buscar(lambda r: r.codigo == codigo_restaurante)
        if not restaurante:
            return "Restaurante " + codigo_restaurante + " no encontrado"

        if restaurante.agregar_producto(nombre, precio, tipo):
            return "Producto '" + nombre + "' agregado al menu de " + restaurante.nombre
        else:
            return "Tipo de producto no valido"

    def buscar_restaurante_cercano(self, zona_cliente, productos_solicitados):
        print("\nBuscando restaurante mas cercano...")
        print("   Cliente en: " + zona_cliente)
        print("   Productos solicitados: " + str(productos_solicitados))

        restaurantes_con_productos = []
        
        for restaurante in self.restaurantes.buscar_todos(lambda r: True):
            tiene_todos = True
            productos_faltantes = []
            
            for producto in productos_solicitados:
                producto_encontrado = False
                for categoria, items in restaurante.menu.items():
                    for item in items:
                        if item['nombre'].lower() == producto.lower():
                            producto_encontrado = True
                            break
                    if producto_encontrado:
                        break
                
                if not producto_encontrado:
                    tiene_todos = False
                    productos_faltantes.append(producto)
            
            if tiene_todos:
                restaurantes_con_productos.append(restaurante)
                print("   " + restaurante.nombre + " (Zona: " + restaurante.zona + ") - TIENE todos los productos")
            else:
                print("   " + restaurante.nombre + " (Zona: " + restaurante.zona + ") - FALTAN: " + str(productos_faltantes))

        if not restaurantes_con_productos:
            print("   Ningun restaurante tiene todos los productos solicitados")
            return None, 0

        print("\n   Calculando distancias desde " + zona_cliente + ":")
        distancias, _ = self.mapa.dijkstra(zona_cliente)
        
        restaurante_cercano = None
        min_distancia = float('inf')
        
        for restaurante in restaurantes_con_productos:
            distancia = distancias.get(restaurante.zona, float('inf'))
            print("   " + restaurante.nombre + " (" + restaurante.zona + "): " + str(distancia) + "km")
            
            if distancia < min_distancia:
                min_distancia = distancia
                restaurante_cercano = restaurante

        if restaurante_cercano:
            print("   MAS CERCANO: " + restaurante_cercano.nombre + " (" + restaurante_cercano.zona + ") - " + str(min_distancia) + "km")
            return restaurante_cercano, min_distancia
        else:
            print("   No se pudo encontrar restaurante cercano")
            return None, 0

    def buscar_domiciliario_cercano(self, zona_restaurante):
        print("\nBuscando domiciliario mas cercano...")
        print("   Restaurante en: " + zona_restaurante)

        domiciliarios_disponibles = self.domiciliarios.buscar_todos(
            lambda d: d.disponible
        )

        if not domiciliarios_disponibles:
            print("   No hay domiciliarios disponibles")
            return None, 0

        distancias, _ = self.mapa.dijkstra(zona_restaurante)
        
        print("   Calculando distancias desde " + zona_restaurante + ":")
        domiciliario_cercano = None
        min_distancia = float('inf')
        
        for domiciliario in domiciliarios_disponibles:
            distancia = distancias.get(domiciliario.zona, float('inf'))
            print("   " + domiciliario.nombre + " (" + domiciliario.zona + "): " + str(distancia) + "km")
            
            if distancia < min_distancia:
                min_distancia = distancia
                domiciliario_cercano = domiciliario

        if domiciliario_cercano:
            print("   MAS CERCANO: " + domiciliario_cercano.nombre + " (" + domiciliario_cercano.zona + ") - " + str(min_distancia) + "km")
            return domiciliario_cercano, min_distancia
        else:
            print("   No se pudo encontrar domiciliario cercano")
            return None, 0

    def crear_pedido(self, codigo_cliente, productos):
        cliente = self.clientes.buscar(lambda c: c.codigo == codigo_cliente)
        if not cliente:
            return "Cliente no encontrado"

        resultado = self.buscar_restaurante_cercano(cliente.zona, productos)
        if not resultado or resultado[0] is None:
            return "No hay restaurantes con los productos solicitados"
        
        restaurante, distancia_cliente_restaurante = resultado

        self.contador_pedidos += 1
        pedido = Pedido("P" + str(self.contador_pedidos).zfill(3), cliente, restaurante, productos)
        pedido.distancia_total = distancia_cliente_restaurante

        resultado_domiciliario = self.buscar_domiciliario_cercano(restaurante.zona)
        if resultado_domiciliario and resultado_domiciliario[0] is not None:
            domiciliario, distancia_restaurante_domiciliario = resultado_domiciliario
            pedido.domiciliario = domiciliario
            pedido.cambiar_estado("ASIGNADO")
            pedido.distancia_total += distancia_restaurante_domiciliario
            domiciliario.disponible = False
            domiciliario.pedido_actual = pedido
            
            print("\nSimulando envio en camino...")
            for i in range(3):
                print("   Pedido " + pedido.codigo + " en camino... " + str(i+1) + "/3")
                time.sleep(1)
            pedido.cambiar_estado("EN_CAMINO")
            
            mensaje = "Pedido " + pedido.codigo + " creado y asignado a " + domiciliario.nombre
        else:
            mensaje = "Pedido " + pedido.codigo + " creado pero no hay domiciliarios disponibles"

        self.pedidos_activos.enqueue(pedido)
        cliente.historial_pedidos.append(pedido)
        
        return (mensaje + "\n" +
                "Restaurante: " + restaurante.nombre + " (Zona: " + restaurante.zona + ")\n" +
                "Distancia total: " + str(pedido.distancia_total) + "km")

    def entregar_pedido(self):
        if self.pedidos_activos.esta_vacia():
            return "No hay pedidos activos para entregar"

        pedido = self.pedidos_activos.dequeue()
        pedido.cambiar_estado("ENTREGADO")

        if pedido.domiciliario:
            pedido.domiciliario.disponible = True
            pedido.domiciliario.pedido_actual = None
            print("   " + pedido.domiciliario.nombre + " ahora esta disponible")

        self.pedidos_entregados.push(pedido)
        return "Pedido " + pedido.codigo + " entregado exitosamente"

    def cancelar_pedido(self, codigo_pedido):
        pedidos_temp = []
        pedido_encontrado = None

        while not self.pedidos_activos.esta_vacia():
            pedido = self.pedidos_activos.dequeue()
            if pedido.codigo == codigo_pedido:
                pedido_encontrado = pedido
                pedido.cambiar_estado("CANCELADO")
                if pedido.domiciliario:
                    pedido.domiciliario.disponible = True
                    pedido.domiciliario.pedido_actual = None
                self.pedidos_cancelados.push(pedido)
            else:
                pedidos_temp.append(pedido)

        for pedido in pedidos_temp:
            self.pedidos_activos.enqueue(pedido)

        if pedido_encontrado:
            return "Pedido " + codigo_pedido + " cancelado exitosamente"
        else:
            return "Pedido " + codigo_pedido + " no encontrado en activos"

    def mostrar_estado(self):
        print("\n" + "="*50)
        print("ESTADO DEL SISTEMA")
        print("="*50)
        
        clientes = self.clientes.buscar_todos(lambda c: True)
        restaurantes = self.restaurantes.buscar_todos(lambda r: True)
        domiciliarios = self.domiciliarios.buscar_todos(lambda d: True)

        print("Clientes registrados:", len(clientes))
        for cliente in clientes:
            print("  -", cliente)

        print("\nRestaurantes registrados:", len(restaurantes))
        for restaurante in restaurantes:
            print("  -", restaurante)

        print("\nDomiciliarios registrados:", len(domiciliarios))
        for domiciliario in domiciliarios:
            print("  -", domiciliario)

        print("\nPedidos activos:", self.pedidos_activos.size)
        temp = []
        while not self.pedidos_activos.esta_vacia():
            pedido = self.pedidos_activos.dequeue()
            temp.append(pedido)
            print("  -", pedido)
        
        for pedido in temp:
            self.pedidos_activos.enqueue(pedido)

        print("\nPedidos entregados:", self.pedidos_entregados.size)
        temp_pila = Pila()
        while not self.pedidos_entregados.esta_vacia():
            pedido = self.pedidos_entregados.pop()
            temp_pila.push(pedido)
            print("  -", pedido)
        
        while not temp_pila.esta_vacia():
            self.pedidos_entregados.push(temp_pila.pop())

        print("\nPedidos cancelados:", self.pedidos_cancelados.size)
        temp_pila2 = Pila()
        while not self.pedidos_cancelados.esta_vacia():
            pedido = self.pedidos_cancelados.pop()
            temp_pila2.push(pedido)
            print("  -", pedido)
        
        while not temp_pila2.esta_vacia():
            self.pedidos_cancelados.push(temp_pila2.pop())

        print("\nHistorial por cliente:")
        for cliente in clientes:
            if cliente.historial_pedidos:
                print("  ", cliente.nombre + ":", len(cliente.historial_pedidos), "pedidos")

    def historial_por_zona(self, zona):
        print("\nHISTORIAL COMPLETO ZONA " + zona + ":")
        
        pedidos_zona = []
        
        temp_activos = []
        while not self.pedidos_activos.esta_vacia():
            pedido = self.pedidos_activos.dequeue()
            temp_activos.append(pedido)
            if pedido.cliente.zona == zona:
                pedidos_zona.append(pedido)
        
        for pedido in temp_activos:
            self.pedidos_activos.enqueue(pedido)
        
        temp_entregados = Pila()
        while not self.pedidos_entregados.esta_vacia():
            pedido = self.pedidos_entregados.pop()
            temp_entregados.push(pedido)
            if pedido.cliente.zona == zona:
                pedidos_zona.append(pedido)
        
        while not temp_entregados.esta_vacia():
            self.pedidos_entregados.push(temp_entregados.pop())
        
        temp_cancelados = Pila()
        while not self.pedidos_cancelados.esta_vacia():
            pedido = self.pedidos_cancelados.pop()
            temp_cancelados.push(pedido)
            if pedido.cliente.zona == zona:
                pedidos_zona.append(pedido)
        
        while not temp_cancelados.esta_vacia():
            self.pedidos_cancelados.push(temp_cancelados.pop())

        if pedidos_zona:
            for pedido in pedidos_zona:
                print("   -", pedido)
        else:
            print("   - No hay pedidos en la zona " + zona)
        
        return pedidos_zona