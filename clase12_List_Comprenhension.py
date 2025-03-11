"""
 Estructura:

 lista=[operacion for x in iterable if condición ]
"""

from annotated_types import LowerCase


numeros_pares=[x**2 for x in range(1,11)]
print("Los cuadrados son->", numeros_pares)

#Celcius a fahrenheit
celcius=[0,10,20,30,40]
fahrenheit=[(temp* 9/5)*32 for temp in celcius]
print("Fahrenheit",fahrenheit)

#números pares
pares=[x for x in range(1,11) if x%2==0]
print("Pares->",pares)

#Matriz
matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print("Matriz->",matriz)

#Row en este caso representa la matriz interna 
inversaMatriz=[[row[i] for row in matriz] for i in range(len(matriz[0]))]
print("Inversa->",inversaMatriz)


#Solucion de inversa sin comprehension List
nueva_inversa=[]
for i in range(len(matriz[0])):
    nueva_inversa_row=[]
    for row in matriz:
        nueva_inversa_row.append(row[i])
    nueva_inversa.append(nueva_inversa_row)           
print(nueva_inversa)


#Ejercicios
#1 Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehension.
base=[1,2,3,4,5]
doble_numero=[num_base*2 for num_base in base]
print(base)
print(doble_numero)

#2 Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.
palabras=["sol", "mar", "montaña", "RIO", "estrella"]
nueva_palabras=[palabra.upper() for palabra in palabras if len(palabra)>3]
otra=[palabra for palabra in palabras if (len(palabra)>=3 and palabra==palabra.upper())]
print(nueva_palabras)
print("Esta es otra->",otra)

#3 Crear un Diccionario con List Comprehension
#Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.
claves=["nombre", "edad", "ocupación"]
valores=["Juan", 30, "Ingeniero"]
diccionario_dato={key:value for (key,value) in zip(claves,valores)} #zip(lista, lista) -> Método que une listas
print(diccionario_dato)

#forma 2
dic_datos={claves[i]:valores[i] for i in (range(len(claves)))}
print(dic_datos)

#4. Anidación de List Comprehensions
#Dada una lista de listas (una matriz):
matriz_dada = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

transpuesta=[[x[i] for x in matriz_dada] for i in range(len(matriz_dada[0]))]
print(matriz_dada)
print(transpuesta)

#5 Extraer Información de una Lista de Diccionarios
# Dada una lista de diccionarios que representan personas: 
# Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.

personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

ciudadanos=[item["nombre"] for item in personas if item["edad"]>30 and item["ciudad"]=="Madrid"]
print(ciudadanos)

#6 List Comprehension con un else
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transformados = [x * 2 if x % 2 == 0 else x for x in numeros] #Si el número no cumple la condición en este caso se agrega sin operación
print("Números transformados:", transformados)