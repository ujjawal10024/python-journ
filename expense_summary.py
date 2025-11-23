print("=== Expense Summary Dashboard ===")

try:
    with open("expenses.txt", "r") as file:
        lines = file.readlines()

    if not lines:
        print("No expenses found.")
    else:
        total = 0
        print("\nALL Expenses:\n")

        for line in lines:
            print(line.strip())

            # Line format: date | Rs amount | reason
            parts =  line.split("|")
            amount_part = parts[1].strip().replace("Rs","").strip()
            total += float(amount_part)

        print("\n----------------------------")
        print(f"Total Expenses: Rs {total}")
        print(f"Total Entries: {len(lines)}")
        print("----------------------------")

except FileNotFoundError:
    print("expenses.txt file not found. Please add some expenses first.")