class Auto:
    def __init__(self, marca, modelo, precio):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
        self.estado=True
    
    def compra(self):

        self.estado=False
    
