numbers=[1,2,3,4,5,6]

#for desde lista
for i in numbers:
    print("Aqui el valor de i=",i)

#for con range
for a in range(0,10):
    print(a)

#for con if
fruits=["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
for fruit in fruits:
    if fruit=="Naranja":
        print("Naranja encontrada")

# While
x=0
while (x<5):
    if x==2:
        x+=1 #Si el contador no sube dentro del if queda en un bucle infinito
        continue
    #continue -> Salta una iteración
    if x==4:
        break 
    #break -> Rompe el while
    print("Esto es while",x)
    x+=1
