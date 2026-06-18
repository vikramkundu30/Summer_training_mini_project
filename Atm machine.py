def check_balance(balance):
    print(f"Your account balance is ${balance}")
def deposit(balance):
    amount = float(input("Enter the amount to deposit: $"))
    balance += amount
    print(f"Deposited ${amount}. \nYour new balance is ${balance}")
    return balance
def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: $"))
    if amount <= balance:
        balance -= amount
        print(f"Withdrew ${amount}. \nYour new balance is ${balance}")
balance = 0
while True:
  print("----------------------------")
  print("--------ATM--MACHINE--------")
  print("1. Check Balance")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Exit")
  print("----------------------------")
  print("----------------------------")
  choice = input("Enter your choice (1/2/3/4): ")
  if choice == "1":
        check_balance(balance)
  elif choice == "2":
        balance = deposit(balance)
  elif choice == "3":
        balance = withdraw(balance)
  elif choice == "4":
        print("Thank you for using the ATM. Have a nice day!")
        break
  else:
        print("Invalid choice. Please select a valid option.")

