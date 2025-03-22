#Las definimos con def

def greet():
    print("Hola mundo")

greet()

#Funcion con parametro -> Si no es enviado el total de parametros que se requieren saldra error
def saludo(name):
    print(f"Hola {name}")

saludo("Diego")

#Valores por defecto en funcion
def fullName(name,lastName="Avellaneda"): # Despues del igual escribimos el valor por defecto ej: lastName="Avellaneda"
    print(f"Hola {name} {lastName}")

fullName("Diego") # -> Solo enviamos el nombre y el apellido lo tomara como el valor por efecto
fullName("Sandra","Londoño") 
fullName(lastName="Alvarez",name="Samsung") # -> Podemos enviar los parametros en desorden identificando cada dato 