# Son similares a los arrays
todo = ["Viajar", "Museo", "Hotel"]

print(todo)
print(f"Tipo de dato de la lista: {type(todo)}")

#Acceder a un elemento de la lista
print(todo[0])
print(todo[-1])

#Slicing -> Rebanar   
cadena="Hola soy Diego"
print(cadena[5]) #Posición exacta
print(cadena[5:]) #Desde la posición 5 en adelante
print(cadena[:5]) #Desde 0 hasta la posición 5 sin incluirla
print(cadena[::2]) #Toda la cadena saltando de 2 en 2
print(cadena[:6:2]) #De 0 a 6 sin incluirla saltando de 2 en 2 


#Agregar elementos a lista .append(elemento_que_queremos_agregar)
lista=["a","b"]
lista.append("c")
print(lista)

#Agregar elemento a lista en un indice especifico
lista.insert(3,"Diego")
print(lista)

#Consultar indice de un elemento en la lista -> lista.index(elemento)
print(lista.index("Diego"))



numbers=[5, 20, 3.2, 50, 7]

#Encontrar el elemento mayor -> max
print("El número mayor es: ",max(numbers))

#Encontrar el elemento menor -> min
print("El número menor es: ",min(numbers))


#Eliminar elementos de lista
del numbers[-1]
print(numbers)

del numbers[:3] #Elimina desde el 0 hasta el 2 sin incluirlo
print(numbers)


