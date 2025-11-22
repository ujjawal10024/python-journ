from datetime import datetime

print("=== Smart Expense Tracker ===")

while True:
    amount = input("Enter expense amount (or 'q' to quit): ")

    if amount.lower() == "q":
        print("Exiting tracker...")
        break
    reason = input("Enter reason: ")
    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    entry = f"{date} | Rs {amount} | {reason}\n"

    with open("expenses.txt" , "a") as file:
        file.write(entry)

        print(" Expense saved!")

        choice = input("Add another? (yes/no): ")
        if choice.lower() != "yes":
            print("Goodbye ")
            break