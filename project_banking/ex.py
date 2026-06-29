import csv
import os
import deposit as dp
import withdraw as wd
import balance as bl
from customers import Customer

FIELDS = ["Name","Age","Username","Email","Password","Balance"]

# ---------------- Create CSV ----------------

with open("userlist.csv", "a+", newline="") as file:
    file.seek(0)
    writer = csv.DictWriter(file, fieldnames=FIELDS)
    if file.read() == "":
        writer.writeheader()

# ---------------- Load Customers ----------------

def load_customers():
    customers = []
    with open("userlist.csv", "r", newline="") as file:
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

    return customers
# ---------------- Save Customers ----------------

def save_customers(customers):
    with open("userlist.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        for user in customers:
            writer.writerow({
                "Name": user.name,
                "Age": user.age,
                "Username": user.username,
                "Email": user.email,
                "Password": user.password,
                "Balance": user.balance
            })
# ---------------- Main Program ----------------

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
            customers = load_customers()
            username = input("Enter Username: ").strip().lower()
            found = False
            for person in customers:
                if person.username == username:
                    found = True
                    break
            if found:
                print("Username already exists.")
                continue
            name = input("Enter Name: ")
            try:
                age = int(input("Enter Age: "))
            except Exception as msg:
                print(msg)
                continue
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            try:
                balance = int(input("Enter Opening Balance: "))
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
            save_customers(customers)
            print("Signup Successful!")
        
                # ---------------- Login ----------------

        case 2:
            customers = load_customers()
            username = input("Enter Username: ").strip().lower()
            password = input("Enter Password: ")
            logged_user = None

            for user in customers:
                if username == user.username and password == user.password:
                    logged_user = user
                    break
            if logged_user is None:
                print("Invalid Username or Password")
                continue
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
                    # -------- Deposit --------
                    case 1:
                        dp.deposit(logged_user)
                        save_customers(customers)
                    # -------- Withdraw --------

                    case 2:
                        wd.withdraw(logged_user)
                        save_customers(customers)
                    # -------- Balance --------

                    case 3:
                        bl.balance(logged_user)
                    # -------- Logout --------

                    case 4:
                        print("Logout Successful!")
                        break
                    case _:
                        print("Invalid Choice")

        # ---------------- Exit ----------------

        case 3:
            print("Thank You!")
            break
        case _:
            print("Enter Valid Choice")