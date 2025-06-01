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
        amount = float(input("What is the amount? "))
        category = input("What is the category? ").lower()
        dateofentry = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(trackerdata, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([dateofentry, amount, category])
        print("Expense added!")

    elif menu == "view all expenses":
        with open(trackerdata, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                date = row[0]
                amount = row[1]
                category = row[2]
                print(f"Date: {date}, Amount: {amount}, Category: {category}")

    elif menu =="update an expense":
        with open(trackerdata, 'r', newline='') as file:
            reader = csv.reader(file)
            expenses = list(reader)





    menu = input(menutext).lower()