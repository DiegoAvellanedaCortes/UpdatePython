name=input("Ingresa tu nombre: ")

age=input("Ingresa tu edad: ")

#Todos los datos ingresados con input son String str

print(name)
print(age)
print(type(name))
print(type(age))

#Si queremos operar tenemos que colocar el tipo de dato antes:
ageInt=int(input("Ingresa tu edad "))
print(f"Edad con Int {ageInt, type(ageInt)}")