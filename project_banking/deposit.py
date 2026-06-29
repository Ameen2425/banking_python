class Deposit:

    def __init__(self):

        self.amount = 0

    def deposit(self, user):

        try:

            self.amount = int(input("Enter Deposit Amount : "))

        except Exception as msg:

            print(msg)
            return

        if self.amount <= 0:

            print("Invalid Amount")
            return

        user.balance = user.balance + self.amount

        print("Deposit Successful")
        print("Current Balance :", user.balance)
