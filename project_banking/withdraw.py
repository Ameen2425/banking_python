class Withdraw:

    def __init__(self):

        self.amount = 0

    def withdraw(self, user):

        try:

            self.amount = int(input("Enter Withdraw Amount : "))

        except Exception as msg:

            print(msg)
            return False

        if self.amount <= 0:

            print("Invalid Amount")
            return False

        if self.amount > user.balance:

            print("Insufficient Balance")
            return False

        user.balance = user.balance - self.amount

        print("Withdrawal Successful")
        print("Current Balance :", user.balance)

        return True