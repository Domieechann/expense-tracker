# Developer: Dominic A. Aquino
# Expense Tracker - Installment 3: The Tracker Does Math

print("============================================================")
print("\t   EXPENSE TRACKER")
print("\t   Know where your money goes.")
print("============================================================")
print("\n Welcome! This is your personal expense tracker.\n")

print("MAIN MENU")
print("  [1] Add an expense" "\t" "(coming soon)")
print("  [2] View all expenses" "\t" "(coming soon)")
print("  [3] Show total spent" "\t" "(coming soon)")
print("  [4] Exit" "\t\t" "(coming soon)")

print("============================================================")

name = input("What is your name?: ")
print("Welcome,", name, "lets log two expenses.")

subtotal = 0

item1 = input("first expense?: ")
amount1 = float(input("How much?: "))
subtotal = subtotal + amount1

item2 = input("second expense?: ")
amount2 = float(input("how much?: "))
subtotal = subtotal + amount2

tax_percent = float(input("Tax rate %?: "))
budget = float(input("Your budget?: "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

print("============================================================")
print("SUMMARY")
print(f"  - {item1}:\t\t${amount1}")
print(f"  - {item2}:\t\t${amount2}")
print(f"Subtotal:\t\t${subtotal}")
print(f"Average:\t\t${average}")
print(f"Tax ({tax_percent}%):\t\t${tax}")
print(f"Grand total:\t\t${total}")
print(f"Over budget?:\t\t{over_budget}")
print(f"Left in budget:\t\t${left}")
print("============================================================")
print("Made by: Dominic A. Aquino  |  Installment 3")
print("============================================================")