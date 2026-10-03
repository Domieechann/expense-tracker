# Developer: Dominic A. Aquino
#installment 2
#Expense Tracker - Installment 2: Talking to the User

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
print("Made by: Dominic A. Aquino  |  1st Laboratory")
print("============================================================")

#installment 2

name = input("What is your name?: ")
print ("Welcome," , name , "lets log two expenses.")

item1 = input ("first expense?: ")
amount1 = float(input("How much?: "))

item2 = input ("second expense?: ")
amount2 = float(input("how much?: "))

total = amount1 + amount2
print("Total expenses for", name, ":", total)

average = total / 2

print("============================================================")
print("SUMMARY")
print(f"  - {item1}:     ${amount1}")
print(f"  - {item2}:     ${amount2}")
print(f"Total spent:    ${total}")
print(f"Average:        ${average}")
print("============================================================")
print("Made by: Dominic A. Aquino  |  Installment 2")
print("============================================================")

