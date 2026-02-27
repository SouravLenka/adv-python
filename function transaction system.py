# transaction system using functions, make functions for login, deposit, withdraw, check balance, transaction history

accounts = {
    "sourav": {"password": "pass123", "balance": 0, "transaction": []},
    "chiru": {"password": "abc", "balance": 1000, "transaction": []},
    "sai": {"password": "123", "balance": 500, "transaction": []}
}

attempts = 0
max_attempts = 3

def login(accounts):
    global attempts
    while attempts < max_attempts:
        uid = input("Enter User ID: ")
        pwd = input("Enter Password: ")

        if uid in accounts and accounts[uid]["password"] == pwd:
            print("Login Successful!")
            return uid
        else:
            attempts += 1
            print("Invalid ID or Password. Attempts left:", max_attempts - attempts)

    if attempts == max_attempts:
        print("Too many wrong attempts. Login blocked.")
        return None

def deposit(balance, transactions):
    amt = int(input("Enter deposit amount: "))
    balance += amt
    transactions.append("Deposited: " + str(amt))
    print("Amount Deposited")
    return balance, transactions

def withdraw(balance, transactions):
    amt = int(input("Enter the withdrawal amount: "))
    if amt <= balance:
        balance -= amt
        transactions.append("Withdraw: " + str(amt))
    else:
        print("Insufficient balance")
    return balance, transactions

def check_balance(balance):
    print("Current Balance :", balance)

def transaction_history(transactions):
    print("\nTransaction History")
    if len(transactions) == 0:
        print("No Transaction History")
    else:
        for t in transactions:
            print(t)

current_user = login(accounts)

if current_user:
    # Local references to the specific user's data
    user_data = accounts[current_user]
    balance = user_data["balance"]
    transactions = user_data["transaction"]

    while True:
        print(f"\nLogged in as: {current_user}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Transaction History")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice : "))
            if choice == 1:
                balance, transactions = deposit(balance, transactions)
            elif choice == 2:
                balance, transactions = withdraw(balance, transactions)
            elif choice == 3:
                check_balance(balance)
            elif choice == 4:
                transaction_history(transactions)
            elif choice == 5:
                # Save data back to the dictionary before exiting (though it's mutated in place via lists)
                accounts[current_user]["balance"] = balance
                print("Thank you for using the system")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
