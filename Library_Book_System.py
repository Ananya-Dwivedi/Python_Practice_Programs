class Book:

    def __init__(self,title,author,is_available=True):

        self.title=title
        self.author=author
        self.is_available=is_available

# __str__ is Python's way of saying "when someone prints this object, show them this string instead.

    def __str__(self):  
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} — {status}"
    
class Library:
    def __init__(self,name):
        self.name=name 
        self.books=[]
    
    def add_book(self,book):
        self.books.append(book)  # obj book is getting added as a list element .
        print(f"{book.title} added to {self.name}")
        return self.books
        

    def checkout_book(self,title):

        for book in self.books:
            if book.title == title:
                if not book.is_available:
                   raise ValueError(f"The book {book.title} is already been checked out .")
                book.is_available=False
                print(f"The book is added successfully.")
            return

        raise ValueError(f"{title} not in the library. ")
                    
      
    def return_book(self,title):
        for book in self.books:
            if book.title ==title:

                if book.is_available:
                    raise ValueError(f"{title} wasn't checked out. ")
                book.is_available=True
                print(f"The book is returned successfully.")
            return
        raise ValueError(f"{title} not in the library. ")

    def available_books(self):
        print(f"Available Books are : \n")
        for book in self.books:
            if book.is_available :
                print(f"{book.title} By {book.author}")

        
    def save_to_file(self):
        
        with open("library.txt", "a") as f:
            for book in self.books:
                status = "Available" if book.is_available else "Checked Out"
                f.write(f"{book.title} | {book.author} | {status}\n")
        print("Library saved to library.txt")

    def load_from_file(self):
        
        try:
            with open("library.txt", "r") as f:
                data = f.readlines()
                print(f"\nLoaded data for {self.name}:")
                for item in data:
                    print(f" - {item.strip()}")
        except FileNotFoundError:
            print("No saved file found — save first")


lib = Library("City Library")

b1 = Book("Harry Potter", "Rowling")
b2 = Book("Clean Code", "Martin")
b3 = Book("The Alchemist", "Coelho")

# print(b1)
# print(b2)
# print(b3)
# b3.is_available=False
# print(b3)

print("---------------------------------")


lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)



try:
    lib.checkout_book("Clean Code")       # should work
    lib.checkout_book("Clean Code")       # should fail — already checked out
except ValueError as e:
    print(f"Error: {e}")

try:
    lib.checkout_book("Invisible Book")   # should fail — not found
except ValueError as e:
    print(f"Error: {e}")

try:
    lib.return_book("Harry Potter")   # should fail — never checked out
except ValueError as e:
    print(f"Error: {e}")
       # now return it — should work
lib.available_books()             

lib.save_to_file()
lib.load_from_file()