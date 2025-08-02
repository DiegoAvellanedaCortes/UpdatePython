class Book:
    def __init__(self, autor, title):
        self.autor=autor
        self.title=title
        self.available=True
    
    def borrow(self, user):
        if self.available:
            self.available=False
            print(f"El libro {self.title} fue prestado a {user}")
        else:
            print(f"El libro {self.title} no esta disponible")

    def return_book(self):
        self.available=True
        print(f"El libro {self.title} fue regresado con exito")

