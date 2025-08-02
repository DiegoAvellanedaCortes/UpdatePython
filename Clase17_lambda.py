#Lambda -> Funciones anonimas indicamos entrada y salida  ej:  nombre= lambda x:x+1 
#                                                                      Entrada:Salida                                
def pedir_numeros():
    a=float(input("Ingresa un número-> "))
    b=float(input("Ingresa un número-> "))
    return a,b

suma=lambda a,b :a+b
a,b=pedir_numeros()
print(suma(a,b))

multiplicacion=lambda a,b:a*b
print(multiplicacion(a,b))


#Listas, map y Lambda
lista=[1,2,3,4]
cuadrados=list(map(lambda x:x**3, lista))
print(cuadrados)