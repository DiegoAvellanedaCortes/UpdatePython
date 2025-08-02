class Vehiculo:
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price
        self.is_available=True
    
    def sell(self):
        if self.is_available:
            self.is_available=False
            print(f"El vehiculo {self.brand} ha sido vendido")
        else:
            print(f"El vehiculo {self.brand} no esta disponible")
    
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    """Método que debe ser implementado por la o las clases hijas (subclase)
    
       con raise=> levantamos una excepción 
    """

    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la clase hija	")
    
    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la clase hija")

  #Pasamos como parametro la clase padre
class Car(Vehiculo):

    def start_engine(self):
        if self.is_avalaible:
            return f"El motor del carro {self.brand} esta en marcha"
        else:
            return f"El motor del carro {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_avalaible:
            return f"El motor del carro {self.brand} esta detenido"
        else:
            return f"El motor del carro {self.brand} no esta disponible"

class Bike(Vehiculo):

    def start_engine(self):
        if self.is_avalaible:
            return f"La bicicleta {self.brand} esta en marcha"
        else:
            return f"La bicicleta {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_avalaible:
            return f"La bicicleta {self.brand} esta detenida"
        else:
            return f"La bicicleta {self.brand} no esta disponible"

class Truck(Vehiculo):
    def start_engine(self):
        if self.is_avalaible:
            return f"El camion {self.brand} esta en marcha"
        else:
            return f"El camion {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_avalaible:
            return f"El camion {self.brand} esta detenido"
        else:
            return f"El camion {self.brand} no esta disponible"
        
class Customer():
    def __init__(self, name):
        self.name=name
        self.purchased_vehicles=[]
    
    """
     vehicle:Vehiculo -> quiere decir que vamos a recir un atribuyo (vehiculo) de la clase que esta despues de los dos puntos (:Vehiculo) 
    """

    def buy_vehicle(self, vehicule:Vehiculo): 
        if vehicule.check_available:
            vehicule.sell()
            self.purchased_vehicles.append(vehicule)
        else:
            print(f"El vehiculo {vehicule.brand} no esta disponible")
    
    def inquire_vehicule(self, vehicule:Vehiculo):
        if vehicule.check_available:
            available="Disponible"
        else:
            available="No disponible"
        print(f"El Vehiculo {vehicule.brand} se encuentra en estado=> {available} y cuesta {vehicule.get_price()}")

class Dealership():
    def __init__(self):
        self.inventory=[]
        self.customers=[]

    def add_vehicles(self, vehicle:Vehiculo):
        self.inventory.append(vehicle)
        print(f"El Vehiculo {vehicle.brand} ha sido agregado al inventario")
    
    def add_customer(self, customer:Customer):
        self.customers.append(customer)
        print(f"El cliente con el nombre {customer.name} ha sido añadido")

    def show_avaliable_vehicles(self):
        print("\nVehiculos disponibles:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"    Vehiculo=> {vehicle.brand} Precio: {vehicle.get_price()}")

#Creamos Vehiculos
car1=Car("Mercedez", 2025, 100000000)
bike1=Bike("Shimano", 2020, 1000000)
truck1=Truck("Ford",2025, 200000000)

#Creamos cliente
customer1=Customer("Diego")

"""
    1. Creamos el consesionario
    2. Agregamos los vehiculos
    3. Agregamos los clientes
"""

dealership1=Dealership()
dealership1.add_vehicles(car1)
dealership1.add_vehicles(bike1)
dealership1.add_vehicles(truck1)

dealership1.add_customer(customer1)

#Mostrar Vehiculos
dealership1.show_avaliable_vehicles()

customer1.inquire_vehicule(car1)
customer1.buy_vehicle(car1)

dealership1.show_avaliable_vehicles()
