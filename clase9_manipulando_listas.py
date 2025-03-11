a=[1,2.3]

#Forma NO adecuada
b=a

b[1]=5  #Modificamos b pero la forma de crear la lista no es adecuada entonces tienen la misma referencia en memoria por lo tanto se modifican las 2

print(a)
print(b)

# id() -> metodo para conocer el id del espacio en memoria
print("Id A ->",id(a))
print("Id B ->",id(b))

#Forma Adecuada de crear una lista partiendo de otra
c=a[:]
print("Id C ->",id(c))