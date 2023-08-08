class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def perimetro(self):
        base = abs(self.punto2.x - self.punto1.x)
        altura = abs(self.punto2.y - self.punto1.y)
        return 2 * (base + altura)

    def area(self):
        base = abs(self.punto2.x - self.punto1.x)
        altura = abs(self.punto2.y - self.punto1.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.punto2.x - self.punto1.x)
        altura = abs(self.punto2.y - self.punto1.y)
        return base == altura


# Crear instancias de Rectangulo
punto_a = Punto(0, 0)
punto_b = Punto(4, 3)
rectangulo1 = Rectangulo(punto_a, punto_b)


print(f"Rectángulo 1: \nPerímetro:,{rectangulo1.perimetro()},\n Área:,{rectangulo1.area()}")
print("¿Es cuadrado?", rectangulo1.es_cuadrado())
