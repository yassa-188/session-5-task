from classes import Library, Book, Member, StaffMember

library = Library()

book1 = Book("1984", "George Orwell", "1234567890", available=True, library=library)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321", available=True, library=library)
book1.display_info()

member1 = Member("John Doe", "M001")
member2 = Member("Jane Smith", "M002")
member1.borrow_book(library, book1)
member2.borrow_book(library, book2)
member1.return_book(library, book1)
staff1 = StaffMember("Alice", "M100", "S001")
staff1.add_book(library, book1)
library.list_books()