#Initial Commit

import csv
from datetime import datetime
import os

trackerdata = "expensetracker.csv"
menutext = (
    "Add a new expense.\n"
    "View all expenses.\n"
    "Update an expense.\n"
    "Delete an expense.\n"
    "View summary of expenses.\n"
    "View summary of expenses.\n"
    "View summary of expenses for specific month.\n"
    "Please choose an option:  "
)
menu = input(menutext).lower()

while menu != "exit":
    if menu == "add a new expense":
        try:
            with open(trackerdata, 'r', newline='') as file:
                reader = csv.reader(file)
                ids = [int(row[0]) for row in reader if row and row[0].isdigit()]
                next_id = max(ids) + 1 if ids else 1
        except FileNotFoundError:
            next_id = 1
        amount = float(input("What is the amount? "))
        category = input("What is the category? ").lower()
        dateofentry = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(trackerdata, 'a', newline='') as file:
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

                if new_category:
                    expense[3] = new_category
                if new_amount:
                    expense[2] = new_amount

                expenses[i] = expense
                break

        if not found:
            print("Expense ID not valid.")
        else:
            with open(trackerdata, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(expenses)
            print("Expenses updated")






    menu = input(menutext).lower()