🚴‍♂️ Sistema de Gestión de Pedidos a Domicilio
Materia: Estructuras de Datos

📋 Descripción

Sistema de Gestión de domicilios desarrollado a partir de la implementación manual de estructuras de datos vistas en clase.
Este Sistema Permite gestionar el ciclo completo de un pedido: desde la solicitud del cliente hasta la entrega, con asignación automática por proximidad geográfica.


Integrates del equipo de trabajo:
| Nombre                             | Rol                              |
| :--------------------------------- | :------------------------------- |
| **Daniel De Jesus Codina Ortiz**   | Desarrollo principal|
| **Isaac Gómez Montero**            | Lógica del sistema               |
| **Yeisson Stiven Marriaga Rojano** | Estructuras y archivos de clases |
| **Diego Alejandro Holguín**        | Organización y documentación     |



 Estructuras de Datos Implementadas
| Estructura         | Archivo    | Uso                                                      | Justificación                                                 |
| :----------------- | :--------- | :------------------------------------------------------- | :------------------------------------------------------------ |
| **Lista Enlazada** | `Lista.py` | Almacenamiento de clientes, restaurantes y domiciliarios | Permite crecimiento dinámico y búsquedas personalizadas       |
| **Cola FIFO**      | `Cola.py`  | Gestión de pedidos activos                               | Procesa los pedidos por orden de llegada (First-In-First-Out) |
| **Pila LIFO**      | `Pila.py`  | Historial de pedidos entregados y cancelados             | Acceso rápido a los pedidos más recientes (Last-In-First-Out) |
| **Grafo**          | `grafo.py` | Mapa de zonas y algoritmo de Dijkstra                    | Representa conexiones geográficas y calcula rutas óptimas     |


## 💡 **Decisiones Técnicas**

### 🔹 Algoritmo de Dijkstra

**Motivo de elección:**  
El algoritmo de Dijkstra fue implementado por su alta eficiencia en el **cálculo de rutas más cortas** entre diferentes zonas del mapa, optimizando el tiempo de entrega y la asignación de domiciliarios.

**Ventajas principales:**
- ⚙️ Eficiente en grafos ponderados basados en distancias reales.  
- 🎯 Garantiza la obtención del camino óptimo entre puntos.  
- 🌍 Se adapta fácilmente a representaciones geográficas del mapa de Santa Marta.


### 🔹 Gestión de Estados de Pedidos

**Implementación:**  
Se diseñó una **máquina de estados** dentro de la clase `Pedido`, permitiendo controlar de forma estructurada el ciclo de vida de cada pedido.

**Flujo de estados:**  
`PENDIENTE → ASIGNADO → EN_CAMINO → ENTREGADO / CANCELADO`

**Ventaja principal:**  
 Ofrece un **control preciso** sobre las transiciones de estado, evitando errores lógicos y garantizando un seguimiento coherente del pedido desde su creación hasta la entrega final.



## ⚙️ **Funcionalidades Implementadas**

| Estado | Descripción |
|:--------|:-------------|
| ✅ | **Registro y gestión** de clientes, restaurantes y domiciliarios |
| ✅ | **Búsqueda por proximidad geográfica** utilizando el algoritmo de **Dijkstra** |
| ✅ | **Gestión completa de pedidos:** crear, asignar, entregar y cancelar |
| ✅ | **Sistema de menús por categorías:** entradas, platos fuertes, postres y bebidas |
| ✅ | **Historial de pedidos** por zona y por cliente |
| ✅ | **Simulación de entregas** en tiempo real |
| ✅ | **Visualización del mapa** de zonas y sus conexiones |



## 🔄 **Flujo del Sistema**

El proceso general del sistema sigue una secuencia lógica que abarca desde la solicitud del cliente hasta la finalización del pedido:

1. 🧍‍♂️ **El cliente realiza un pedido** desde su zona correspondiente.  
2. 🍽️ **El sistema identifica** el restaurante más cercano con disponibilidad de los productos solicitados.  
3. 🚴 **Se asigna automáticamente** el domiciliario más próximo al restaurante.  
4. 🔁 **El pedido avanza** a través de sus estados hasta su entrega final.  
5. ✅ **El domiciliario queda disponible** nuevamente para recibir nuevos pedidos.



## 🗺️ **Mapa de Zonas Implementado**

El sistema incluye las principales zonas de **Santa Marta**, utilizadas para representar la red geográfica donde se gestionan los pedidos y se calculan las rutas más cortas mediante el **algoritmo de Dijkstra**.

**Zonas incluidas:**
- 🏙️ Centro Histórico  
- 🌊 Rodadero  
- 🌅 Bello Horizonte  
- 🌴 Mamatoco  
- 🚴 Gaira  
- 🐠 Taganga  
- 🌇 Pozos Colorados  

> 📍 Las distancias entre zonas son **reales y aproximadas**, utilizadas para el cálculo de **rutas óptimas** mediante el algoritmo de Dijkstra.



## 🧪 **Pruebas y Validación**

El sistema desarrollado implementa diversos mecanismos de validación para asegurar la **consistencia**, la **integridad de los datos** y el **correcto funcionamiento** del flujo de pedidos.

**Aspectos verificados:**
- 🗺️ **Existencia de zonas** registradas en el mapa.  
- 🔢 **Códigos únicos** para cada entidad (clientes, restaurantes y pedidos).  
- 🍽️ **Disponibilidad de productos** en los restaurantes antes de aceptar un pedido.  
- 🔄 **Estados válidos** dentro del flujo de pedidos (`PENDIENTE → ASIGNADO → EN_CAMINO → ENTREGADO / CANCELADO`).  
- 🚴 **Disponibilidad de domiciliarios activos** para nuevas asignaciones.

> ✅ Estas validaciones garantizan que cada operación se ejecute bajo condiciones controladas y sin conflictos en los datos.



Por ultimo Nuestro Link de Nuestro Repositorio.

https://github.com/danielcodina4583-lab/sistema-pedidos-domicilio
