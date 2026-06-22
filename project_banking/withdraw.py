def withdraw(user):
    try:
        amount = int(input("Enter amount: "))
    except Exception as msg:
        print(msg)
        amount = int(input("Enter amount: "))
    else:
        print(amount, "is valid")
    finally:
        print("amount enetered is valid")
    if amount <= user['Balance']:
        user['Balance'] -= amount
        print("Withdrawal Successful")
    else: ## if amount is greater than balance
        print("Insufficient Balance")