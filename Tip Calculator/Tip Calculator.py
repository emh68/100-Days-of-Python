# Tip calculator to assist in determining how much each person owes including tip

print("welcome to the tip calculator!")
bill_total = float(input("What is your total bill? $"))
tip_amount = float(input("What percent tip would you like to give? Ex.: 10, 12, or 15? "))
num_people = int(input("How many people will split the bill? "))

# Calculate total bill plus tip
bill_with_tip = bill_total * (1 + tip_amount / 100)
each_person_bill = round(bill_with_tip / num_people, 2)

print(f"Each person should pay: ${each_person_bill}")
