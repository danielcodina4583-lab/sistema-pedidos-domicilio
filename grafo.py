class Grafo:
    def __init__(self):
        self.zonas = {}
        self.distancias = {}

    def agregar_zona(self, zona):
        if zona not in self.zonas:
            self.zonas[zona] = []
            print(f"Zona '{zona}' agregada al mapa")
            return True
        return False

    def conectar_zonas(self, zona1, zona2, distancia):
        if zona1 in self.zonas and zona2 in self.zonas:
            if zona2 not in self.zonas[zona1]:
                self.zonas[zona1].append(zona2)
            if zona1 not in self.zonas[zona2]:
                self.zonas[zona2].append(zona1)

            self.distancias[(zona1, zona2)] = distancia
            self.distancias[(zona2, zona1)] = distancia
            print(f"Conexion {zona1} <--[{distancia}km]--> {zona2}")
            return True
        return False

    def obtener_vecinos(self, zona):
        return self.zonas.get(zona, [])

    def obtener_distancia(self, zona1, zona2):
        return self.distancias.get((zona1, zona2), float('inf'))

    def dijkstra(self, inicio):
        if inicio not in self.zonas:
            return {}, {}
        
        distancias = {vertice: float('inf') for vertice in self.zonas}
        predecesores = {vertice: None for vertice in self.zonas}
        distancias[inicio] = 0
        visitados = set()
        
        while len(visitados) < len(self.zonas):
            vertice_actual = None
            min_distancia = float('inf')
            
            for vertice in self.zonas:
                if vertice not in visitados and distancias[vertice] < min_distancia:
                    min_distancia = distancias[vertice]
                    vertice_actual = vertice
            
            if vertice_actual is None:
                break
            
            visitados.add(vertice_actual)
            
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino in visitados:
                    continue
                    
                distancia = self.obtener_distancia(vertice_actual, vecino)
                nueva_distancia = distancias[vertice_actual] + distancia
                
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = vertice_actual
        
        return distancias, predecesores

    def zona_mas_cercana(self, inicio, zonas_destino):
        distancias, _ = self.dijkstra(inicio)

        zona_cercana = None
        min_distancia = float('inf')

        for zona in zonas_destino:
            if zona in distancias and distancias[zona] < min_distancia:
                min_distancia = distancias[zona]
                zona_cercana = zona

        return zona_cercana

    def mostrar_mapa(self):
        print("\n MAPA DE LA Ciudad DE SANTA MARTA:")
        for zona, vecinos in self.zonas.items():
            conexiones = []
            for vecino in vecinos:
                distancia = self.obtener_distancia(zona, vecino)
                conexiones.append(f"{vecino}({distancia}km)")
            print(f"  {zona}: {', '.join(conexiones)}")