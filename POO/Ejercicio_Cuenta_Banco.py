class Cuenta:
    def __init__(self, balance, acount_holder):
        self.balance=balance
        self.acount_holder=acount_holder
        self.activate=True

    def consultar_saldo(self):
        print(f"{self.acount_holder}-> el saldo actual de tu cuentaes {self.balance}")

    def depositar(self, valor):
        if self.activate:
            self.balance+=valor
            print(f"{self.acount_holder}-> Recargaste tu cuenta con {valor}")
        else:{
            print(f"{self.acount_holder}-> Tu cuenta no esta activa")
        }
    def desactivar_cuenta(self):
        if self.activate:
            self.activate=False
            print(f"{self.acount_holder}-> Cuenta desactivada")
        else:
            print(f"{self.acount_holder}->Tu cuenta se encuentra desactivada")

    def activar_cuenta(self):
        if self.activate==False:
            self.activate=True
            print(f"{self.acount_holder}->Activamos tu cuenta")
        else:
            print(f"{self.acount_holder}->Tu cuenta ya esta activa")

    def retirar(self, valor):
        if self.activate:
            if valor<=self.balance:
                self.balance -=valor
                print(f"{self.acount_holder}->Retiraste {valor}, tu saldo es {self.balance}")
            else:
                print(f"{self.acount_holder}->No tienes dinero para este retiro")
        else:
            print(f"{self.acount_holder}->Tu cuenta no esta activa")

cuenta1=Cuenta(1000, "Diego")
cuenta2=Cuenta(500, "Sandy")

cuenta1.consultar_saldo()
cuenta1.retirar(50)

cuenta2.depositar(100)
cuenta2.desactivar_cuenta()
cuenta2.consultar_saldo()
