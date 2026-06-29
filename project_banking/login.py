from filehandler import FileHandler
from deposit import Deposit
from withdraw import Withdraw
from balance import Balance


class Login:

    def __init__(self):

        self.file = FileHandler()

    def login(self):

        customers = self.file.load_users()

        username = input("Enter Username : ").strip().lower()
        password = input("Enter Password : ")

        found = False

        for user in customers:

            if username == user.username and password == user.password:

                found = True

                print("================================")
                print(" Login Successful ")
                print("================================")

                while True:

                    print("""
1. Deposit
2. Withdraw
3. Balance
4. Logout
""")

                    option = int(input("Enter your choice : "))

                    match option:

                        case 1:

                            deposit = Deposit()

                            deposit.deposit(user)

                            self.file.save_users(customers)

                            if deposit.amount > 0:

                                self.file.save_transaction(
                                    user.username,
                                    "Deposit",
                                    deposit.amount,
                                    user.balance
                                )

                        case 2:

                            withdraw = Withdraw()

                            withdraw.withdraw(user)

                            self.file.save_users(customers)

                            if withdraw.amount > 0:

                                self.file.save_transaction(
                                user.username,
                                "Withdraw",
                                 withdraw.amount,
                                 user.balance
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