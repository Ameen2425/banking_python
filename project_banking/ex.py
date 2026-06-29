from signup import Signup
from login import Login

signup = Signup()
login = Login()

print("===================================")
print("      WELCOME TO PYTHON BANK")
print("===================================")

while True:

    print("""
1. Signup
2. Login
3. Exit
""")

    try:

        choice = int(input("Enter Your Choice : "))

    except Exception as msg:

        print(msg)
        continue

    match choice:

        case 1:

            signup.signup()

        case 2:

            login.login()

        case 3:

            print("===================================")
            print("Thank You For Visiting Python Bank")
            print("===================================")
            break

        case _:

            print("Invalid Choice")