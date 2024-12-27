from booklendsystem import BookLendingSystem
from admin import Admin
from book import Book
from member import Member
import utils

# Create instances of the classes
system = BookLendingSystem()
system.loginAdmin()
while system.isAdmin:
    # Display the menu
    utils.MENUS = ["List Book","Add Book","Edit Book", "Lend Book", "Return Book", "Add Member", "Exit"]
    choose = system.showMenu()
    if int(choose) - 1 is utils.MENUS.index("Add Book"):
        system.addBook()
    elif int(choose) - 1 is utils.MENUS.index("Edit Book") :
        system.editBook()
    elif int(choose) - 1 is utils.MENUS.index("List Book") :
        system.listBook()
    elif int(choose) - 1 is utils.MENUS.index("Lend Book"):
        system.lendBook()
    elif int(choose) - 1 is utils.MENUS.index("Return Book"):
        system.returnBook()
    elif int(choose) - 1 is utils.MENUS.index("Add Member"):
        Member.addMember()
    elif int(choose) - 1 is utils.MENUS.index("Exit"):
        print("Bye")
        break
    else:
        print("Error input")

    

