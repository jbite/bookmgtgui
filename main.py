from booklendsystem import BookLendingSystem
from admin import Admin
from book import Book
from member import Member

# Create instances of the classes
system = BookLendingSystem()
system.loginAdmin()
while system.isAdmin:
    # Display the menu
    menus = ["List Book","Add Book","Edit Book", "Lend Book", "Return Book", "Add Member", "Exit"]
    choose = system.showMenu()
    if int(choose) - 1 is menus.index("Add Book"):
        system.addBook()
    elif int(choose) - 1 is menus.index("Edit Book") :
        system.editBook()
    elif int(choose) - 1 is menus.index("List Book") :
        system.listBook()
    elif int(choose) - 1 is menus.index("Lend Book"):
        system.lendBook()
    elif int(choose) - 1 is menus.index("Return Book"):
        system.returnBook()
    elif int(choose) - 1 is menus.index("Add Member"):
        Member.addMember()
    elif int(choose) - 1 is menus.index("Exit"):
        print("Bye")
        break
    else:
        print("Error input")

    

