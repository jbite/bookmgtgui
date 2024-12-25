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