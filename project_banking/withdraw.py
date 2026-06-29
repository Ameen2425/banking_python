from bank import Bank


class Withdraw(Bank):

    def __init__(self):

        self.amount = 0

    # ---------- Polymorphism ----------

    def operation(self):

        print("Withdraw Operation")

    # ---------- Withdraw ----------

    def withdraw(self, user):

        self.operation()

        try:

            self.amount = int(input("Enter Withdraw Amount : "))

        except Exception as msg:

            print(msg)
            return False

        if self.amount <= 0:

            print("Invalid Amount")
            return False

        if self.amount > user.get_balance():

            print("Insufficient Balance")
            return False

        balance = user.get_balance()

        balance = balance - self.amount

        user.set_balance(balance)

        print("Withdrawal Successful")
        print("Current Balance :", user.get_balance())

        return True