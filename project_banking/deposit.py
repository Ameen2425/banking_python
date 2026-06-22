def deposit(user):
    try:
        amount = int(input("Enter amount: "))
    except Exception as msg:
        print(msg)
        amount = int(input("Enter amount: "))
    else:
        print(amount, "is valid")
    finally:
        print("amount enetered is valid")
    user['Balance'] += amount
    print("Amount Deposited Successfully")