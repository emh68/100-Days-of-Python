
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? " + "(S, M, or L)" + "\n")
add_pepperoni = input("Do you want pepperoni? " + "(Y or N)" + "\n")
extra_cheese = input("Do you want extra cheese? " + "(Y or N)" + "\n")


bill = 0

if size.upper() == "S":
    bill += 15
elif size.upper() == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni.upper() == "Y":
    if size.upper() == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese.upper() == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")




















