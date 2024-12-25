from booklendsystem import BookLendingSystem
from admin import Admin
from book import Book
from member import Member

# Create instances of the classes
system = BookLendingSystem()
# book = Book()  # You can create a Book instance if needed
member = Member()
admin = Admin()

# Display the menu
system.showMenu()