#Initial Commit

import csv
from datetime import datetime
import os

trackerdata = "expensetracker.csv"

menu = input(" Add a new expense.\n View all expenses.\n Update an expense.\n Delete an expense. \n View summary of expenses.\n View summary of expenses for specific month.\n Please choose an option: ").lower()

while menu != "exit":
    if menu == "add a new expense":
        amount = float(input("What is the amount? "))
        category = input("What is the category? ").lower()
        dateofentry = datetime.now()
        with open(trackerdata, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([dateofentry, amount, category])
        print("Expense added")

