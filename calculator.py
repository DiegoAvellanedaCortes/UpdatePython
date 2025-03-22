def sum(a, b):
    return a + b


def rest(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b

def pedirNumeros():
    num1 = float(input("Ingresa un número -> "))
    num2 = float(input("Ingresa un número -> "))
    return num1,num2

def calculator():
    while True:
        print("Selecciona una opción")
        print("1. Suma \n2. Resta \n3. Multiplicación \n4. División \n5. Salir")
        try:
            seleccion = int(input("Opción=> "))
            if seleccion in [1,2,3,4]:
                num1,num2=pedirNumeros()
                if seleccion == 1:
                    print(f"La suma de {num1} y {num2} es: ", sum(num1, num2))
                elif seleccion == 2:
                    print(f"La resta de {num1} y {num2} es: ", rest(num1, num2))
                elif seleccion == 3:
                    print(f"La multiplicación de {num1} y {num2} es: ", mul(num1, num2))
                elif seleccion == 4:
                    print(f"La división de {num1} y {num2} es: ", div(num1, num2))
                elif seleccion == 5:
                    break
                else:
                    print("Opción no valida, intenta nuevamente")
        except:
            print("No puedo solucionar esto")


calculator()
