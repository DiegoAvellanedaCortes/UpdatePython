class Usuario:

    #Constructor -> Acá damos los atributos de la clase
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    #Métodos -> Definimos las tareas 
    def greet(self): #self -> Referencia al objeto que llama al método
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")

#Creamos cada objeto -> Instancia de la clase
usuario1=Usuario("Diego", 27)
usuario2=Usuario("Sandy", 25)

#Llamamos al método
usuario1.greet()
usuario2.greet()

