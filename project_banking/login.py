import re
from bank import Bank
from filehandler import FileHandler
from deposit import Deposit
from withdraw import Withdraw
from balance import Balance


class Login(Bank):

    def __init__(self):
        self.file = FileHandler()

    # ---------- Polymorphism ----------
    def operation(self):
        print("Login Operation")

    # ---------- Login ----------
    def login(self):

        self.operation()

        customers = self.file.load_users()

        # ---------- Username ----------
        while True:
            username = input("Enter Username : ").strip().lower()

            if re.fullmatch(r"[a-zA-Z0-9]{5,15}", username):
                break

            print("Invalid Username (5-15 letters and numbers only)")

        # ---------- Password ----------
        password = input("Enter Password : ").strip()

        found = False

        for user in customers:

            if user.get_username() == username and user.get_password() == password:

                found = True

                print("\nLogin Successful")

                while True:

                    print("""
1. Deposit
2. Withdraw
3. Balance
4. Logout
""")

                    try:
                        option = int(input("Enter Your Choice : "))
                    except ValueError:
                        print("Please enter a valid number.")
                        continue

                    match option:

                        case 1:

                            deposit = Deposit()

                            success = deposit.deposit(user)

                            if success:

                                self.file.save_users(customers)

                                self.file.save_transaction(
                                    user.get_username(),
                                    "Deposit",
                                    deposit.amount,
                                    user.get_balance()
                                )

                        case 2:

                            withdraw = Withdraw()

                            success = withdraw.withdraw(user)

                            if success:

                                self.file.save_users(customers)

                                self.file.save_transaction(
                                    user.get_username(),
                                    "Withdraw",
                                    withdraw.amount,
                                    user.get_balance()
                                )

                        case 3:

                            balance = Balance()

                            balance.show_balance(user)

                        case 4:

                            print("Logout Successful")
                            break

                        case _:

                            print("Invalid Choice")

                break

        if not found:

            print("Invalid Username or Password")