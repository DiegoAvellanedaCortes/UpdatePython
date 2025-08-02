from auto import Auto
from usuario import Usuario


class Concensionario:
    def __init__(self, dinero):
        self.dinero=dinero
        self.autos=[]
        self.usuarios=[]
    
    def consultar_saldo_Concesionario(self):
        print(f"Saldo total {self.dinero}")

    def compra(self,auto):
        if auto.precio <= self.dinero:
            self.autos.append(auto)
            self.dinero-=auto.precio
            print(f"Compramos el {auto.marca} por un valor de {auto.precio}, Saldo actual {self.dinero}")
        else:
            print("El dinero no es suficiente")

    def consultar_autos(self):
        contador=0
        for carro in self.autos:
            contador+=1
            print(f"{contador} => Marca: {carro.marca} | Modelo: {carro.modelo} | Precio: {carro.precio}")

    def venta(self, carro, usuario):
        for auto in self.autos:
            if auto==carro:
                if auto.precio<=usuario.presupuesto:
                    print(f"Puedes comprar el {carro.marca} | Modelo: {carro.modelo} | Precio: {carro.precio}")
                    compra=int(input("Quieres comprar el carro? 1. Si 2. No =>"))
                    if compra==1:
                        self.autos.remove(auto)
                        self.dinero+= carro.precio
                else:
                    print(f"No puedes comprar el {carro.marca} | Modelo: {carro.modelo} | Precio: {carro.precio}")

    
auto1=Auto("Mazda", 2025, 30000000)
auto2=Auto("Audi", 2024, 40000000)

usuario1=Usuario("Sandy", 200000000)

concesionario=Concensionario(100000000)
concesionario.consultar_saldo_Concesionario()
concesionario.compra(auto1)
concesionario.compra(auto2)
concesionario.consultar_saldo_Concesionario()
print("--------------------------------------Consulta Carros")
concesionario.consultar_autos()

concesionario.venta(auto2,usuario1)
print("--------------------------------------Consulta Carros")
concesionario.consultar_autos()
concesionario.consultar_saldo_Concesionario()
