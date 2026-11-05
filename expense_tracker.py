import json

# Load expenses
try:
    file = open("expenses.json", "r")
    expenses = json.load(file)
    file.close()
except:
    expenses = []


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Total Expenses")
    print("5. Category Summary")
    print("6. Update Expense")
    print("7. Delete Expense")
    print("8. Exit")

    choice = input("Enter your choice: ")


    # 1. ADD EXPENSE
    if choice == "1":

        print("\n--- Add Expense ---")

        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        date = input("Enter date: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }

        expenses.append(expense)

        file = open("expenses.json", "w")
        json.dump(expenses, file, indent=4)
        file.close()

        print("Expense added successfully!")


    # 2. VIEW EXPENSES
    elif choice == "2":

        print("\n--- Expense History ---")

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            for expense in expenses:

                print("--------------------")
                print("Amount:", expense["amount"])
                print("Category:", expense["category"])
                print("Description:", expense["description"])
                print("Date:", expense["date"])


    # 3. SEARCH EXPENSE
    elif choice == "3":

        print("\n--- Search Expense ---")

        search = input("Enter category to search: ")

        for expense in expenses:

            if expense["category"].lower() == search.lower():

                print("--------------------")
                print("Amount:", expense["amount"])
                print("Category:", expense["category"])
                print("Description:", expense["description"])
                print("Date:", expense["date"])


    # 4. TOTAL EXPENSES
    elif choice == "4":

        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print("\nTotal Expenses:", total)


    # 5. CATEGORY SUMMARY
    elif choice == "5":

        print("\n--- Category Summary ---")

        food = 0
        travel = 0
        shopping = 0
        other = 0

        for expense in expenses:

            if expense["category"].lower() == "food":
                food = food + expense["amount"]

            elif expense["category"].lower() == "travel":
                travel = travel + expense["amount"]

            elif expense["category"].lower() == "shopping":
                shopping = shopping + expense["amount"]

            else:
                other = other + expense["amount"]


        print("Food:", food)
        print("Travel:", travel)
        print("Shopping:", shopping)
        print("Other:", other)


    # 6. UPDATE EXPENSE
    elif choice == "6":

        print("\n--- Update Expense ---")

        for i in range(len(expenses)):

            print(i + 1, expenses[i]["category"],
                  expenses[i]["amount"])


        number = int(input("Enter expense number to update: "))

        number = number - 1

        if number >= 0 and number < len(expenses):

            expenses[number]["amount"] = float(
                input("Enter new amount: ")
            )

            expenses[number]["category"] = input(
                "Enter new category: "
            )

            expenses[number]["description"] = input(
                "Enter new description: "
            )

            expenses[number]["date"] = input(
                "Enter new date: "
            )


            file = open("expenses.json", "w")
            json.dump(expenses, file, indent=4)
            file.close()

            print("Expense updated successfully!")

        else:
            print("Invalid expense number.")


    # 7. DELETE EXPENSE
    elif choice == "7":

        print("\n--- Delete Expense ---")

        for i in range(len(expenses)):

            print(i + 1, expenses[i]["category"],
                  expenses[i]["amount"])


        number = int(input("Enter expense number to delete: "))

        number = number - 1

        if number >= 0 and number < len(expenses):

            expenses.remove(expenses[number])

            file = open("expenses.json", "w")
            json.dump(expenses, file, indent=4)
            file.close()

            print("Expense deleted successfully!")

        else:
            print("Invalid expense number.")


    # 8. EXIT
    elif choice == "8":

        print("Thank you for using Expense Tracker!")
        break


    else:

        print("Invalid choice!")