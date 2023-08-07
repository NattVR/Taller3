
class Vehiculo:
    def __init__(self, velocidad_maxima: float, kilometraje: float):
        self.velocidad_maxima: float = velocidad_maxima
        self.kilometraje: float = kilometraje


auto_1 = Vehiculo(200, 120000)
print(auto_1.velocidad_maxima)
print(auto_1.kilometraje)
