import os
import private
import utils
from book import Book

class BookLendingSystem:
    def __init__(self):
        """Read book list from books.json
        """
        books = utils.Rbook()
        self.AvailableBooks = books
        self.isAdmin = False
        self.currentAdmin = []

    def loginAdmin(self):
        username = input("Username: ")
        password = input("Password: ")

        admins = private.ADMIN
        if username in admins:
            if password == admins[username]["passwd"]:
                if username in self.currentAdmin:
                    print(f"{username} is already login.")
                    return False
                else:
                    self.isAdmin = True
                    self.currentAdmin.append("username")
                    print("Login success.")
                return True
        else:
            print("Username or password is not correct.")
            return False
        
    def logoutAdmin(self):
        self.isAdmin = False
        return False
    
    def showMenu(self):
        
        print("\nBook Lending System Menu:")
        for index, option in enumerate(utils.MENUS):
            print(f"{index+1}: {option}")

        choose = input("Choose: ")
        return choose
    
    def listBook(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{"Book Name":<20}{"Credit":>10} ")
        print("*"*30)
        for value in self.AvailableBooks:
            print(f"{self.AvailableBooks[value]["bname"]:<20}\
                {self.AvailableBooks[value]["price"]:>10} ")

    def addBook(self):
        bid = input("Enter Book ID: ")
        bname = input("Enter Book Name: ")
        price = float(input("Enter Book Price: "))
        book = Book(bid=bid,bname=bname,price=price)
        
        if self.AvailableBooks is None:
            print(type(self.AvailableBooks))
            self.AvailableBooks = {}
        self.AvailableBooks[bid] = book.__dict__
        try:
            utils.Wbook(self.AvailableBooks)
            print("Book added successfully!")
        except IOError as e:
            print(e)
            

    def editBook(self):
        self.listBook()
        bid = input("Enter Book ID to edit: ")
        if bid in self.AvailableBooks:
            book = self.AvailableBooks[bid]
            book["bname"] = input("Enter new Book Name: ")
            book["price"] = float(input("Enter new Book Price: "))
            print("Book updated successfully!")
        else:
            print("Book not found!")

    def lendBook(self):
        mid = int(input("Enter Member ID: "))
        bid = int(input("Enter Book ID to lend: "))
        if bid in self.AvailableBooks:
            book = self.AvailableBooks[bid]
            if book["available"] and member["credit"] > book["price"]:
                book["available"] = False
                book["borrower"].append(mid)
                member = member["credit"] - book["price"]
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