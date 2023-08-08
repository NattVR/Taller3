import math

class Circulo:
    def __init__(self, centro: tuple, radio: float):
        self.centro = centro
        self.radio = radio

    def area(self):
        area = self.radio ** 2 * math.pi
        return area

    def perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

    def punto_pertenece(self, punto: tuple):
        distancia_centro_punto = math.sqrt((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2)
        return distancia_centro_punto <= self.radio

if __name__ == "__main__":
    centro = (0, 0)
    radio = 5
    circulo_1 = Circulo(centro, radio)
    area = circulo_1.area()
    perimetro = circulo_1.perimetro()
    print(f"El area del circulo es: {round(area, 2)} y el perimetro: {round(perimetro, 2)}")
    punto = (1, 5)
    if circulo_1.punto_pertenece(punto):
        print(f"El punto {punto} pertenece al círculo.")
    else:
        print(f"El punto {punto} no pertenece al círculo.")
