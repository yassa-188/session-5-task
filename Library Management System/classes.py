class Library:
    def __init__(self):
        self.books = []

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display_info()

    def is_book_in_library(self, book):
            return book in self.books

class Book:
    def __init__(self, title, author, isbn, available, library):
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.available = available
        self.library = library
        library.books.append(self)

    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn
        
    def display_info(self):
        print(f"{self.title} by {self.author} (ISBN: {self.__isbn}) - {'Available' if self.available else 'Not Available'}")

class Member:
    def __init__(self, name, membership_id, borrowed_books=None):
        self.name = name
        self.__membership_id = membership_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
    def get_membership_id(self):
        return self.__membership_id

    def set_membership_id(self, new_id):
        self.__membership_id = new_id

    def borrow_book(self, library, book):
        if not library.is_book_in_library(book):
            print(f"{book.title} is not in the library.")
            return
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed: {book.title}")
        else:
            print(f"{book.title} is not available.")
    
    def return_book(self, library, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned: {book.title}")
        else:
            print(f"{self.name} doesn't have {book.title}.")

class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library, book):
        for existing_book in library.books:
            if existing_book.get_isbn() == book.get_isbn():
                print(f"Book with ISBN {book.get_isbn()} already exists.")
                return
        library.books.append(book)
        print(f"Staff {self.name} added book: {book.title}")
        
