import deposit as dp
import withdraw as wd
import balance as bl


customers = [] ## it is a empty  list
print("====== WELCOME TO OUR BANK ======")
while True: ## enter choices
    print("""
    1. Signup
    2. Login
    3. Exit
    """)
    
    ## it will ask user to enter choice
    choice = int(input("Enter your choice: "))
    match choice:
        case 1: ## signup with details 
            user = {} ## empty dictionary
            user['Name'] = input("Enter your name: ")
            try:
                user['Age'] = int(input("Enter your age: "))
            except Exception as msg: ## if age is not integer in msg:
                print(msg)
                user['Age'] = int(input("Enter your age: "))
            else:
                print(user['Age'], "is valid")
            finally:
                print("You are eligible to open an account")
            user['Username'] = input("Enter your username: ").strip().lower() ## it will convert to lower case
            user['Email'] = input("Enter your email: ")
            user['Password'] = input("Enter your password: ")
            try:
                user['Balance'] = int(input("Enter your balance: "))
            except Exception as msg:
                print(msg)
                user['Balance'] = int(input("Enter your balance: "))
            else:
                print(user['Balance'], "is valid")
            finally:
                print("You are eligible to open an account")
            customers.append(user) ## it will add user to list
            print("Signup Successful!")
        case 2: ## login with user name and password
            username = input("Enter your username: ").strip().lower() ## it will convert to lower case 
            password = input("Enter your password: ")
            for user in customers:
                if username == user['Username'] and password == user['Password']: ## if username and password matchs then login 
                    print("Login Successful!")
                    while True: ##  after login enter choices    
                        print("""
                        1. Deposit
                        2. Withdraw
                        3. Balance
                        4. Logout
                        """)
                        option = int(input("Enter your choice: "))  ## it will ask user to enter choice 
                        match option:  
                            case 1: ## deposit
                                dp.deposit(user)
                            case 2: ## withdraw
                                wd.withdraw(user)
                            case 3: ## balance
                                bl.balance(user)                              
                            case 4: ## logout
                                break 
                            case _: ## if choice is invalid
                                print("Invalid Choice")               
                else: ## if username or password is invalid
                    print("Invalid Username or Password")    
        case 3: ## exit
            break
        case _: ## if choice is invalid
            print("Enter a Valid Choice")
            
            