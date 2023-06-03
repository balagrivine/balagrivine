balance = 2000000
command = input("Perform action >  ")
if command.lower() == "withdraw":
    amount_to_withdraw = int(input("Enter amount >  "))
    while amount_to_withdraw < balance:
        pin = int(input("Enter pin >  "))
        max_attempts = 3
        if pin == 1234:
            print("Successfully withdrawn" + " " + str(amount_to_withdraw))
            print("New account balance is" + " " + str(balance-amount_to_withdraw))
            break
        if pin != 1234:
            max_attempts += 1
            print("Sorry, you entered the wrong pin")
    if amount_to_withdraw > balance:
        print("Sorry, the amount you are trying to withdraw is more than what's in your account.")

elif command.lower() == "deposit":
    amount_to_deposit = int(input("Enter amount >  "))
    prompt = input("Do you want to check balance?  ")
    if prompt == "yes":
        balance = balance + amount_to_deposit
        print("Your balance is" + " " + "Ksh." + " " + str(balance))

