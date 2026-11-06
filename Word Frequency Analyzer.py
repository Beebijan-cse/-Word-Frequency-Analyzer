import os

FILE_NAME = "expenses.txt"
SEP = "|"


def load():
    expenses = []
    if not os.path.exists(FILE_NAME):
        return expenses

    file = open(FILE_NAME, "r")
    for line in file:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(SEP)
        expenses.append({"item": parts[0], "amount": float(parts[1]), "category": parts[2]})
    file.close()
    return expenses


def save(expenses):
    file = open(FILE_NAME, "w")
    for e in expenses:
        file.write(e["item"] + SEP + str(e["amount"]) + SEP + e["category"] + "\n")
    file.close()


def add(expenses):
    item = input("Item name: ").strip()
    if item == "":
        print("Item name can't be empty.")
        return
    if SEP in item:
        print("Item name can't contain |")
        return

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("That's not a number.")
        return

    if amount <= 0:
        print("Amount must be more than 0.")
        return

    category = input("Category (Food, Transport, Bills, Other): ").strip().title()
    if category == "":
        category = "Other"

    expenses.append({"item": item, "amount": amount, "category": category})
    save(expenses)
    print("Added " + item + " ($" + str(round(amount, 2)) + ")")


def view(expenses):
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    print("\nItem".ljust(20) + "Amount".rjust(10) + "  Category")
    print("-" * 45)
    for e in expenses:
        print(e["item"].ljust(20) + ("$%.2f" % e["amount"]).rjust(10) + "  " + e["category"])


def totals(expenses):
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    sums = {}
    for e in expenses:
        if e["category"] in sums:
            sums[e["category"]] += e["amount"]
        else:
            sums[e["category"]] = e["amount"]

    print("\nTotals by category:")
    total_all = 0
    for cat in sums:
        print("  " + cat.ljust(12) + ("$%.2f" % sums[cat]))
        total_all += sums[cat]

    print("\n  Total: $%.2f" % total_all)


def main():
    expenses = load()

    while True:
        print("\n1. Add  2. View  3. Totals  4. Quit")
        choice = input("Pick an option: ").strip()

        if choice == "1":
            add(expenses)
        elif choice == "2":
            view(expenses)
        elif choice == "3":
            totals(expenses)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Please pick 1-4.")


main()