from sistema_pedidos import SistemaPedidos

def mostrar_menu():
    print("\n" + "="*50)
    print("SISTEMA DE PEDIDOS A DOMICILIO - MENU PRINCIPAL")
    print("="*50)
    print("1. Registrar Cliente")
    print("2. Registrar Restaurante")
    print("3. Registrar Domiciliario")
    print("4. Agregar Producto a Restaurante")
    print("5. Crear Pedido")
    print("6. Entregar Pedido")
    print("7. Cancelar Pedido")
    print("8. Mostrar Estado del Sistema")
    print("9. Mostrar Mapa de Zonas")
    print("10. Mostrar Menus de Restaurantes")
    print("11. Historial por Zona")
    print("0. Salir")
    print("="*50)

def buscar_producto_en_restaurantes(sistema, nombre_producto):
    """Busca un producto por nombre en todos los restaurantes"""
    restaurantes = sistema.restaurantes.buscar_todos(lambda r: True)
    
    for restaurante in restaurantes:
        menu_str = restaurante.obtener_menu()
        lineas = menu_str.split('\n')
        
        for linea in lineas:
            linea = linea.strip()
            if linea.startswith('-') and ':' in linea:
              
                producto_linea = linea[1:].split(':', 1)[0].strip()
               
                if producto_linea.lower() == nombre_producto.lower():
                    return producto_linea  
    return None

def main():
    sistema = SistemaPedidos()
    
    zonas_disponibles = ["Centro Historico", "Rodadero", "Bello Horizonte", 
                         "Mamatoco", "Gaira", "Taganga", "Pozos Colorados"]

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":
            print("\nREGISTRAR CLIENTE")
            codigo = input("Codigo: ")
            nombre = input("Nombre: ")
            print("Zonas disponibles: Centro Historico, Rodadero, Bello Horizonte, Mamatoco, Gaira, Taganga, Pozos Colorados")
            zona = input("Zona: ")
            if zona not in zonas_disponibles:
                print("Error: Zona no válida. Use una de las zonas disponibles.")
                continue
            print(sistema.registrar_cliente(codigo, nombre, zona))

        elif opcion == "2":
            print("\nREGISTRAR RESTAURANTE")
            codigo = input("Codigo: ")
            nombre = input("Nombre: ")
            print("Zonas disponibles: Centro Historico, Rodadero, Bello Horizonte, Mamatoco, Gaira, Taganga, Pozos Colorados")
            zona = input("Zona: ")
            if zona not in zonas_disponibles:
                print("Error: Zona no válida. Use una de las zonas disponibles.")
                continue
            print(sistema.registrar_restaurante(codigo, nombre, zona))

        elif opcion == "3":
            print("\nREGISTRAR DOMICILIARIO")
            codigo = input("Codigo: ")
            nombre = input("Nombre: ")
            print("Zonas disponibles: Centro Historico, Rodadero, Bello Horizonte, Mamatoco, Gaira, Taganga, Pozos Colorados")
            zona = input("Zona: ")
            if zona not in zonas_disponibles:
                print("Error: Zona no válida. Use una de las zonas disponibles.")
                continue
            print(sistema.registrar_domiciliario(codigo, nombre, zona))

        elif opcion == "4":
            print("\nAGREGAR PRODUCTO A RESTAURANTE")
            codigo_rest = input("Codigo del restaurante: ")
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio: "))
            except ValueError:
                print("Error: El precio debe ser un número")
                continue
            print("Tipos: entradas, platos_fuertes, postres, bebidas")
            tipo = input("Tipo: ")
            print(sistema.agregar_producto_restaurante(codigo_rest, nombre, precio, tipo))

        elif opcion == "5":
            print("\nCREAR PEDIDO")
            codigo_cliente = input("Codigo del cliente: ")
            
          
            productos_pedido = []
            print("\n--- AGREGAR PRODUCTOS AL PEDIDO ---")
            print("Escriba el nombre de los productos que desea ordenar")
            print("Escriba 'fin' cuando termine de agregar productos")
            
            while True:
                print(f"\nProductos en pedido: {productos_pedido}")
                nombre_producto = input("Nombre del producto (o 'fin' para terminar): ")
                
                if nombre_producto.lower() == 'fin':
                    break
                
                if not nombre_producto.strip():
                    print("❌ Por favor ingrese un nombre de producto válido")
                    continue
                
                # Buscar el producto en todos los restaurantes
                producto_encontrado = buscar_producto_en_restaurantes(sistema, nombre_producto)
                
                if producto_encontrado:
                    productos_pedido.append(producto_encontrado)
                    print(f" Producto '{producto_encontrado}' agregado al pedido")
                else:
                    print("Producto no encontrado en ningún restaurante")
                    print(" Sugerencia: Verifique el nombre o use la opción 10 para ver los menús disponibles")
            
            if not productos_pedido:
                print("No se agregaron productos al pedido")
                continue
            
            
            print(f"\nCreando pedido con productos: {productos_pedido}")
            print(sistema.crear_pedido(codigo_cliente, productos_pedido))

        elif opcion == "6":
            print("\nENTREGAR PEDIDO")
            print(sistema.entregar_pedido())

        elif opcion == "7":
            print("\nCANCELAR PEDIDO")
            codigo_pedido = input("Codigo del pedido: ")
            print(sistema.cancelar_pedido(codigo_pedido))

        elif opcion == "8":
            sistema.mostrar_estado()

        elif opcion == "9":
            sistema.mapa.mostrar_mapa()

        elif opcion == "10":
            print("\nMENUS DE RESTAURANTES")
            restaurantes = sistema.restaurantes.buscar_todos(lambda r: True)
            for restaurante in restaurantes:
                print(f"\n{restaurante.nombre} ({restaurante.codigo}):")
                menu = restaurante.obtener_menu()
                print(menu)

        elif opcion == "11":
            print("\nHISTORIAL POR ZONA")
            print("Zonas disponibles: Centro Historico, Rodadero, Bello Horizonte, Mamatoco, Gaira, Taganga, Pozos Colorados")
            zona = input("Ingrese la zona: ")
            if zona not in zonas_disponibles:
                print("Error: Zona no válida. Use una de las zonas disponibles.")
                continue
            sistema.historial_por_zona(zona)

        elif opcion == "0":
            print("\nHasta pronto!")
            break

        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()