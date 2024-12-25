class BookLendingSystem:
    def __init__(self):
        self.AvailableBooks = {}

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

class Book:
    def __init__(self):
        self.bid = 0
        self.bname = ""
        self.available = True
        self.borrower = []
        self.price = 0

class Member:
    def __init__(self):
        self.member = {}
        self.mid = 0
        self.mname = ""
        self.lendedBooks = []
        self.mCredit = 0

    def addMember(self):
        mid = int(input("Enter Member ID: "))
        mname = input("Enter Member Name: ")
        mCredit = float(input("Enter Initial Credit: "))
        self.member[mid] = {
            'mname': mname,
            'lendedBooks': [],
            'mCredit': mCredit
        }
        print("Member added successfully!")

    def loginMember(self):
        mid = int(input("Enter Member ID to login: "))
        if mid in self.member:
            print("Member logged in successfully!")
        else:
            print("Member not found!")

    def logoutMember(self):
        print("Member logged out successfully!")

class Admin:
    def __init__(self,aid,username):
        self.aid = 0
        self.username = ""
        self.password = ""
        
    def addAdmin(self):
        pass  # Implementation for adding a new admin

    def addCreditMember(self):
        mid = int(input("Enter Member ID to add credit to: "))
        credit = float(input("Enter amount of credit to add: "))
        if mid in Member.member:  # Assuming Member is an instance of the Member class
            Member.member[mid]['mCredit'] += credit
            print("Credit added successfully!")
        else:
            print("Member not found!")

    def loginAdmin(self):
        pass  # Implementation for admin login

    def logoutAdmin(self):
        pass  # Implementation for admin logout

# Create instances of the classes
system = BookLendingSystem()
# book = Book()  # You can create a Book instance if needed
member = Member()
admin = Admin()

# Display the menu
system.showMenu()