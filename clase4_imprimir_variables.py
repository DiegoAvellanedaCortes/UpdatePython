#sep="algo"
#El caracter que tengamos como propiedad en sep es el que separara los elementos= Hola*soy*Diego sep puede ser cualquier cosa
print("Hola","soy","Diego", sep="*")


#end=""
#Elimina el salto de linea en varios print y los imprime en una unica ej:
print("Nunca", end=" ")
print("pares de aprender")
#Resultado Nunca pares de aprender


#print(f "string") -> Iniciando con la f podemos agregar variables dentro de llaves {} en el String sin tener que concatenar 
name="Diego"
lastname="Avellaneda"
print(f"Nombre: {name} apellido: {lastname}" )

#print con format
municipio="Suesca"
dep="Cun"
print("Vivo en {}, {}".format(municipio,dep))


#Formato especifico, ejemplo :.2f -> imprime solo 2 decimales despues del punto
valor=3.14159
print("Valor: {:.2f}".format(valor))


#imprimir frase con comillas
print("Hola soy 'Diego'") # -> usando diferentes comillas
print("Hola soy \"Diego\"") # -> usando comillas iguales
