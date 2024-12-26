from member import Member
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
