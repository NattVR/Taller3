class Cuenta:
    def __init__(self, numero_cuenta: str, propietarios: str):
        self.numero_cuenta: str = numero_cuenta
        self.propietarios: str = propietarios
        self.balance: float = 0

    def depositar(self, deposito):
        self.balance += deposito
        return deposito

    def retirar(self, cantidad: float):
        if self.balance >= cantidad:
            self.balance -= cantidad
        else:
            cantidad = 0
        return cantidad

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        return cuota

    def mostrar_detalles(self ,deposito, retiro, cuota):
        print(f" Banco*** \n  Detalles de cuenta  \n Número de cuenta:{self.numero_cuenta}\n Propiestario: {self.propietarios} \n Balance actual: ${self.balance} \n Valor depositado:${deposito},\n Valor retirado:${retiro}\n Valor de manejo:${cuota}")

if __name__ == "__main__":
    cuenta_1 = Cuenta("123", "MARCO")
    deposito = cuenta_1.depositar(100)
    retiro = cuenta_1.retirar(50)
    cuota = cuenta_1.aplicar_cuota_manejo()
    cuenta_1.mostrar_detalles(deposito, retiro, cuota)
