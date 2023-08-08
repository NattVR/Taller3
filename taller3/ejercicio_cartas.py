class Carta:
    Pintas = ("1", "2", "3", "4")

    def __init__(self, valor: str, pinta: str):
        self.valor = valor
        self.pinta = pinta

if __name__ == "__main__":
    carta_1 = Carta("23", "3")
    carta_2 = Carta("10", "5")

    print(f"Carta 1: Valor = {carta_1.valor}, Pinta = {carta_1.pinta}")
    print(f"Carta 2: Valor = {carta_2.valor}, Pinta = {carta_2.pinta}")
