import csv
from datetime import datetime
import os

#Menu as variable to reduce re printing
trackerdata = "expensetracker.csv"
menutext = (
    "Add a new expense.\n"
    "View all expenses.\n"
    "Update an expense.\n"
    "Delete an expense.\n"
    "View summary of expenses.\n"
    "View summary of expenses for specific month.\n"
    "Please choose an option:  "
)
#Call back menu
menu = input(menutext).lower()

#Exiting option
while menu != "exit":
    if menu == "add a new expense":
        try:
            with open(trackerdata, 'r', newline='') as file: #Open file to read
                reader = csv.reader(file)
                ids = [int(row[0]) for row in reader if row and row[0].isdigit()]
                next_id = max(ids) + 1 if ids else 1
        except FileNotFoundError: #If file isn't found continue
            next_id = 1
        amount = float(input("What is the amount? "))
        category = input("What is the category? ").lower()
        dateofentry = datetime.now().strftime("%Y-%m-%d %H:%M") #Current date and time but not down to milliseconds
        with open(trackerdata, 'a', newline='') as file: #Amend option to write to file
            writer = csv.writer(file)
            writer.writerow([next_id, dateofentry, amount, category])
        print("Expense added!")

    elif menu == "view all expenses":
        with open(trackerdata, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                id = row[0]
                date = row[1]
                amount = row[2]
                category = row[3]
                print(f"Id: {id} Date: {date}, Amount: {amount}, Category: {category}")

    elif menu =="update an expense":
        with open(trackerdata, 'r', newline='') as file:
            reader = csv.reader(file)
            expenses = list(reader)
        for row in expenses:
            print(f"Id: {row[0]} Date: {row[1]}, Amount: {row[2]}, Category: {row[3]}")
        update_id = input("Which ID would you like to update: ")

        found = False
        for i, expense in enumerate(expenses):
            if expense[0] == update_id:
                found = True

                new_amount = input(f"Enter new amount or press enter to keep current expense at {expense[2]}: ")
                new_category = input(f"Enter new category or press enter to keep current category at {expense[3]}: ")

                #If anything was entered update to new input
                if new_category:
                    expense[3] = new_category
                if new_amount:
                    expense[2] = new_amount

                expenses[i] = expense
                break
        #Error checking
        if not found:
            print("Expense ID not valid.")
        else:
            with open(trackerdata, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(expenses)
            print("Expenses updated")

    elif menu == "delete an expense":
        with open(trackerdata, 'r', newline='') as file:
            reader = csv.reader(file)
            expenses = list(reader)
        for row in expenses:
            print(f"Id: {row[0]} Date: {row[1]}, Amount: {row[2]}, Category: {row[3]}")
        delete_id = input("Which ID would you like to delete: ")

        #Deleting ID
        found = False
        for i, expense in enumerate(expenses):
            if expense[0] == delete_id:
                del expenses[i]
                found = True
                break
        #Error Checking
        if not found:
            print("Please enter valid ID to delete.")
        else:
            for idx, expense in enumerate(expenses, start=1): #Using start 1 to ensure IDs are updated and accurate after deletion
                expense[0] = str(idx)
            with open(trackerdata, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(expenses)
            print("Expense deleted")


    elif menu == "view summary of expenses":
        with open(trackerdata, 'r', newline='') as file:
            reader = csv.reader(file)
            total = 0
            count = 0 #Created count to allow user to know how many records were used
            for row in reader:
                try:
                    amount = float(row[2])
                    total += amount
                    count += 1
                except (ValueError, IndexError):
                    continue
        print(f"Total amount of expenses is ${total:.2f}")
        print(f"Total number of records: {count}")

    elif menu == "view summary of expenses for specific month":
        target_month = input("Enter the month in format YYYY-MM: ") #Using display to ensure user input is correct format as the csv

        with open(trackerdata, 'r', newline='') as file:
            reader = csv.reader(file)
            count = 0
            total = 0

            for row in reader:
                try:
                    date = row[1]
                    amount = float(row[2])

                    if date.startswith(target_month):
                        total += amount
                        count += 1
                except (ValueError, IndexError):
                    continue
        print(f"Total expenses for {target_month}: ${total:.2f}")
        print(f"Total number of records for {target_month}: {count}")


    menu = input(menutext).lower()