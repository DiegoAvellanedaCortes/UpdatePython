class User:
    def __init__(self, name, id_user):
        self.name=name
        self.id_user=id_user
        self.borrow_books=[]

    def borrow_book(self,book):
        if book.available:
            book.borrow(self.name)
            self.borrow_books.append(book)
        else:
            print(f"El libro {book.title} no esta disponible")

    def return_book(self,book):
        if book in self.borrow_books:
            self.borrow_books.remove(book)
            book.return_book()
        else:
            print(f"El libro {book.title} no esta en la lista")
