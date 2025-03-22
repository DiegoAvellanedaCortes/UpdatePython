import random

def seleccion(user, dato):
    if dato == 1:
        print(f"{user}->{dato} Piedra")
    elif dato == 2:
        print(f"{user}->{dato} Papel")
    elif dato == 3:
        print(f"{user}->{dato} Tijera")
    else:
        print("Dato no valido")

def jugar(jugador,pc):
    if jugador == pc:
        print("Empate")
    elif jugador == 1 and pc == 2 or jugador == 2 and pc == 3 or jugador == 3 and pc == 1:
        print("Gana el PC")  
    elif jugador == 1 and pc == 3 or jugador == 2 and pc == 1 or jugador == 3 and pc == 2:
        print("Gana el Jugador")


jugador = int(input("Ingresa una seleccion 1.Piedra 2.Papel 3.Tijera =>"))
pc = random.randint(1, 3)

seleccion("Jugador", jugador)
seleccion("Pc", pc)
jugar(jugador,pc)

