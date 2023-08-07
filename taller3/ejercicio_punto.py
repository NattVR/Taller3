import math


class Punto:
    def __init__(self, coordenada_x: float, coordenada_y: float):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y

    def mostrar(self):
        print(f"El punto en el plano es:({self.coordenada_x},{self.coordenada_y})")

    def mover(self, coordenada_x1: float, coordenada_y2: float):
        self.coordenada_x = coordenada_x1
        self.coordenada_y = coordenada_y2

    def calcular_distancia(self, punto_compara):
        distancia = math.sqrt((punto_compara[0]-self.coordenada_x)**2 + (punto_compara[1]-self.coordenada_y)**2)
        return distancia


if __name__ == "__main__":
    punto_1 = Punto(4, 6)
    punto_1.mostrar()
    punto_1.mover(5, 8)
    punto_1.mostrar()
    punto_compara = (4, 2)
    distancia = punto_1.calcular_distancia(punto_compara)
    print(f"La distancia entre el nuevo punto y el punto a comparar {punto_compara} es {distancia}")
