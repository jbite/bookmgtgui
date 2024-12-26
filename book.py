class Book:
    def __init__(self,bid=0,bname="",available=True,borrower=[],price=0):
        self.bid = bid
        self.bname = bname
        self.available = available
        self.borrower = borrower
        self.price = price

# import json

# books ={}
# for i in range(1,10):
#     books[int(i)] = Book(i,i,True,[],300.0).__dict__


# with open("books.json",'w') as f:
#     json.dump(books,f)


