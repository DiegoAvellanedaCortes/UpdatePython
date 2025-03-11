#Diccionarios

numbers={
    1:"uno",
    2:"dos",
    3:"tres"
}

print(numbers[1])

data={
    "name":"Diego",
    "age":27,
    "Mun":"Suesca"
}

print(data)

#Eliminar dato
del data["Mun"]
print(data)


print("Keys",data.keys())
print("Valores",data.values())
print("Clave, Valor",data.items()) #Retorna una tupla (key, value)

contacs={
    "Diego":{
        "Full_name":"Diego Avellaneda",
        "Stature":1.73,
        "Age":27
    },
    "Carla":{
        "Full_name":"Carla la peligrosa",
        "Stature":1.60,
        "Age":29
    },
}

print(contacs["Carla"])


