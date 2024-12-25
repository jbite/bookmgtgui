class BookLendingSystem:
    def __init__(self):
        self.AvailableBooks = {}
        self.isAdmin = False

    def loginAdmin(self):
        username = input("Username: ")
        password = input("Password: ")

        if username == "admin" and password == "A12345!":
            self.isAdmin = True
            return True
        else:
            return False
        
    def logoutAdmin(self):
        self.isAdmin = False
        return False
    
    def showMenu(self):
        print("\nBook Lending System Menu:")
        print("1. Add Book")
        print("2. Edit Book")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Add Member")
        print("6. Exit")

    def addBook(self):
        bid = int(input("Enter Book ID: "))
        bname = input("Enter Book Name: ")
        price = float(input("Enter Book Price: "))
        book = Book()
        book.bid = bid
        book.bname = bname
        book.price = price
        self.AvailableBooks[bid] = book
        print("Book added successfully!")

    def editBook(self):
        bid = int(input("Enter Book ID to edit: "))
        if bid in self.AvailableBooks:
            book = self.AvailableBooks[bid]
            book.bname = input("Enter new Book Name: ")
            book.price = float(input("Enter new Book Price: "))
            book.available = input("Is the book available (True/False): ").lower() == "true"
            print("Book updated successfully!")
        else:
            print("Book not found!")

    def lendBook(self):
        mid = int(input("Enter Member ID: "))
        bid = int(input("Enter Book ID to lend: "))
        if bid in self.AvailableBooks:
            book = self.AvailableBooks[bid]
            if book.available:
                book.available = False
                book.borrower.append(mid)
                print("Book lent successfully!")
            else:
                print("Book is not currently available.")
        else:
            print("Book not found!")

    def returnBook(self):
        mid = int(input("Enter Member ID: "))
        bid = int(input("Enter Book ID to return: "))
        if bid in self.AvailableBooks:
            book = self.AvailableBooks[bid]
            if not book.available and mid in book.borrower:
                book.available = True
                book.borrower.remove(mid)
                print("Book returned successfully!")
            else:
                print("Book was not borrowed by this member.")
        else:
            print("Book not found!")