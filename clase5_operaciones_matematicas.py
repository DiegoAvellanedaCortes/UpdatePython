num1=int(input("Ingresa un número-> "))
num2=int(input("Ingresa un número-> "))

print(f"Suma {num1+num2}")
print(f"Resta {num1-num2}")
print(f"Multiplicación {num1*num2}")
print(f"División {num1/num2}")

#Parte entera de división
print(f"División entera {num1//num2}")

#modulo
print(f"Modulo {num1 % num2}")

#potencia
print(f"Potencia {num1**num2}")

#shortcuts -> atajos
num1+=5
print(f"Suma num1: {num1}")
num1-=5
print(f"Resta num1: {num1}")
num1*=5
print(f"Multiplicación num1: {num1}")
num1/=5
print(f"División num1: {num1}")

#Regla PEMDAS  Parentesis, Exponencia, Multiplicación, División, Adición, Sustracción
operation_1= 2+3*4
operation_2= (2+3)*4
operation_3= (2+3)*(4**2)/8-1
print(operation_1)
print(operation_2)
print(operation_3)

