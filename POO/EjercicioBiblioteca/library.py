from itertools import count
from book import Book
from user import User


class Library:
    def __init__(self):
        self.books=[]
        self.users=[]
    
    def add_books(self,book):
        self.books.append(book)
        print(f"El libro {book.title} fue agregado")

    def add_user(self,user):
        self.users.append(user)
        print(f"Usuario {user.name} creado")

    def show_avaliable_books(self):
        contador=0
        print("-------Libros disponibles-------")
        for book in self.books:
            if book.available:
                print(f"El libro '{book.title}' de {book.autor}")
                contador+=1
        if contador==0:
            print(f"No tenemos libros disponibles.")    
            

#Crear libros
book1=Book("Diego", "Alguito")
book2=Book("Alexander", "Era de hielo 2")

#Crear Usuario
user1=User("Sandy",1)

#Creamos bibliote, agregamos libros y usuarios
library=Library()
library.add_books(book1)
library.add_books(book2)
library.add_user(user1)


print("\n----------------------------------")
library.show_avaliable_books()
print("\n----------------------------------")
user1.borrow_book(book2)
user1.borrow_book(book1)
print("\n----------------------------------")
library.show_avaliable_books()
print("\n----------------------------------")
user1.return_book(book1)
library.show_avaliable_books()