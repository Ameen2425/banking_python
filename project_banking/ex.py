import csv
import os
import deposit as dp
import withdraw as wd
import balance as bl
from customers import Customer

customers = []

# ---------------- Load Users ----------------

if os.path.exists("userlist.csv"):

    file = open("userlist.csv", "r", newline="")

    reader = csv.DictReader(file)

    for row in reader:

        user = Customer(
            row["Name"],
            int(row["Age"]),
            row["Username"],
            row["Email"],
            row["Password"],
            int(row["Balance"])
        )

        customers.append(user)

    file.close()

print("====== WELCOME TO OUR BANK ======")

while True:

    print("""
    1. Signup
    2. Login
    3. Exit
    """)

    choice = int(input("Enter your choice: "))

    match choice:

        # ---------------- Signup ----------------

        case 1:

            name = input("Enter your Name: ")

            try:
                age = int(input("Enter your Age: "))
            except Exception as msg:
                print(msg)
                continue

            username = input("Enter Username: ").strip().lower()
            email = input("Enter Email: ")
            password = input("Enter Password: ")

            try:
                balance = int(input("Enter Balance: "))
            except Exception as msg:
                print(msg)
                continue

            user = Customer(
                name,
                age,
                username,
                email,
                password,
                balance
            )

            customers.append(user)

            header = [
                "Name",
                "Age",
                "Username",
                "Email",
                "Password",
                "Balance"
            ]

            file_exists = os.path.exists("userlist.csv")

            file = open("userlist.csv", "a", newline="")

            writer = csv.DictWriter(file, fieldnames=header)
            
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                "Name": user.name,
                "Age": user.age,
                "Username": user.username,
                "Email": user.email,
                "Password": user.password,
                "Balance": user.balance
            })
            file.close()
            print("Signup Successful!")

        # ---------------- Login ----------------

        case 2:
            username = input("Enter Username: ").strip().lower()
            password = input("Enter Password: ")
            found = False
            for user in customers:

                if username == user.username and password == user.password:
                    found = True
                    print("Login Successful!")
                    while True:

                        print("""
                        1. Deposit
                        2. Withdraw
                        3. Balance
                        4. Logout
                        """)

                        option = int(input("Enter your choice: "))

                        match option:
                            case 1:
                                dp.deposit(user)
                            case 2:
                                wd.withdraw(user)
                            case 3:
                                bl.balance(user)
                            case 4:
                                print("Logout Successful!")
                                break
                            case _:
                                print("Invalid Choice")
                    break
            if found == False:
                print("Invalid Username or Password")

        # ---------------- Exit ----------------

        case 3:
            print("Thank You!")
            break
        case _:
            print("Enter a Valid Choice")