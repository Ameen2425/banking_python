import re
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

        # ---------- Username ----------
        while True:
            username = input("Enter Username : ").strip().lower()

            if re.fullmatch(r"[a-zA-Z0-9]{5,15}", username):
                break

            print("Invalid Username (5-15 letters and numbers only)")

        for user in customers:
            if user.get_username() == username:
                print("Username Already Exists")
                return

        # ---------- Name ----------
        while True:
            name = input("Enter Name : ").strip().title()

            if re.fullmatch(r"[A-Za-z ]{3,20}", name):
                break

            print("Invalid Name")

        # ---------- Age ----------
        while True:
            try:
                age = int(input("Enter Age : "))

                if 18 <= age <= 100:
                    break

                print("Age must be between 18 and 100.")

            except ValueError:
                print("Enter a valid age.")

        # ---------- Email ----------
        while True:
            email = input("Enter Email : ").strip()

            if re.fullmatch(
                r"^[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$",
                email,
            ):
                break

            print("Invalid Email")

        # ---------- Password ----------
        while True:
            password = input("Enter Password : ")

            if re.fullmatch(
                r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&]).{8,16}$",
                password,
            ):
                break

            print(
                "Password must contain:\n"
                "- 8 to 16 characters\n"
                "- At least one uppercase letter\n"
                "- At least one lowercase letter\n"
                "- At least one digit\n"
                "- At least one special character (@ # $ % &)"
            )

        # ---------- Opening Balance ----------
        while True:
            try:
                balance = int(input("Enter Opening Balance : "))

                if balance >= 0:
                    break

                print("Balance cannot be negative.")

            except ValueError:
                print("Enter a valid balance.")

        # ---------- Create Customer ----------
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

        print("\nSignup Successful!")