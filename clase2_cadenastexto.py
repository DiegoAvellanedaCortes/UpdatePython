#Formas para representar cadenas

#1 
name="Diego"  #comillas dobles
lastname='Avellaneda      Cortés' #comillas simples
fullname='''  
Diego
Alexander
Avellaneda
'''   #Comillas triples, respetan los saltos de linea 

print(name)
print(lastname)
print(fullname)

# Manipulación de cadenas de texto

print(name[2]) #Las cadenas funcionan como un Listas-> Array
print(name[-2]) #Con los números negativos imprimimos la cadena desde el final al inicio, siendo -1 el ultimo caracter

#Concatenar cadenas
print(name+lastname) 
print(name,lastname) # La coma , agrega un espacio entre las cadenas
print(name.lower()) #Todo el texto en minuscula 
print(name.upper()) #Todo el texto en mayuscula
print("-> ",lastname)
print(lastname.strip()) #Elimina los espacios al inicio de la cadena
