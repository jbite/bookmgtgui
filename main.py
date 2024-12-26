from booklendsystem import BookLendingSystem
from admin import Admin
from book import Book
from member import Member

# Create instances of the classes
system = BookLendingSystem()
system.loginAdmin()
while system.isAdmin:
    # Display the menu
    choose = system.showMenu()
    if int(choose) == 1:
        system.addBook()
    elif int(choose) == 2:
        system.editBook()
    elif int(choose) == 3:
        system.lendBook()
    elif int(choose) == 4:
        system.returnBook()
    elif int(choose) == 5:
        Member.addMember()
    elif int(choose) == 6:
        print("Bye")
        break
    else:
        print("Error input")

    

