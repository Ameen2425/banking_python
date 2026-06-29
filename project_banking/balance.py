from bank import Bank


class Balance(Bank):

    # ---------- Polymorphism ----------

    def operation(self):

        print("Balance Operation")

    # ---------- Balance ----------

    def show_balance(self, user):

        self.operation()
        print("Current Balance:", user.get_balance())
