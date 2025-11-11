class Restaurante:
    def __init__(self, codigo, nombre, zona):
        self.codigo = codigo
        self.nombre = nombre
        self.zona = zona
        self.menu = {
            "entradas": [],
            "platos_fuertes": [],
            "postres": [],
            "bebidas": []
        }
    
    def agregar_producto(self, nombre, precio, tipo):
        if tipo in self.menu:
            self.menu[tipo].append({"nombre": nombre, "precio": precio})
            return True
        return False
    
    def obtener_menu(self):
        menu_str = f"\n MENÚ {self.nombre}:\n"
        for categoria, productos in self.menu.items():
            menu_str += f"  {categoria.upper()}:\n"
            for producto in productos:
                menu_str += f"    - {producto['nombre']}: ${producto['precio']}\n"
        return menu_str
    
    def __str__(self):
        return f"Restaurante {self.codigo}: {self.nombre} (Zona: {self.zona})"