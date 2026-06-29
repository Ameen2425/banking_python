from bank import Bank
from customers import Customer
from filehandler import FileHandler


class Signup(Bank):

    def __init__(self):

        self.file = FileHandler()

    # ---------- Polymorphism ----------

    def operation(self):

        print("Signup Operation")

    # ---------- Signup ----------

    def signup(self):

        self.operation()

        customers = self.file.load_users()

        username = input("Enter Username : ").strip().lower()

        found = False

        for user in customers:

            if user.get_username() == username:

                found = True
                break

        if found:

            print("Username Already Exists")
            return

        name = input("Enter Name : ")

        try:

            age = int(input("Enter Age : "))

        except Exception as msg:

            print(msg)
            return

        email = input("Enter Email : ")

        password = input("Enter Password : ")

        try:

            balance = int(input("Enter Opening Balance : "))

        except Exception as msg:

            print(msg)
            return

        user = Customer(

            name,
            age,
            username,
            email,
            password,
            balance

        )

        customers.append(user)

        self.file.save_users(customers)

        print("Signup Successful")
