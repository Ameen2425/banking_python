from bank import Bank


class Deposit(Bank):

    def __init__(self):

        self.amount = 0

    # ---------- Polymorphism ----------

    def operation(self):

        print("Deposit Operation")

    # ---------- Deposit ----------

    def deposit(self, user):

        self.operation()

        try:

            self.amount = int(input("Enter Deposit Amount : "))

        except Exception as msg:

            print(msg)
            return False

        if self.amount <= 0:

            print("Invalid Amount")
            return False

        balance = user.get_balance()

        balance = balance + self.amount

        user.set_balance(balance)
        print("Deposit Successful")
        print("Current Balance :", user.get_balance())

        return True