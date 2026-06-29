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

        username = input("Enter Username : ").strip().lower()
        password = input("Enter Password : ")

        found = False

        for user in customers:

            if username == user.get_username() and password == user.get_password():

                found = True

                print("Login Successful")

                while True:

                    print("""
1. Deposit
2. Withdraw
3. Balance
4. Logout
""")

                    option = int(input("Enter Your Choice : "))

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

        if found == False:

            print("Invalid Username or Password")