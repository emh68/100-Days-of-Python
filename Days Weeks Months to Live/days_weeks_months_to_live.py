# Calculates how many days, weeks and months a user has left to live if they live to be 90 yrs old
age = input("What is your current age? ")

age = int(age)
days = (32_850 - (age*365))
weeks = (4_680 - (age*52))
months = (1_080 - (age*12))
print(f"You have {days} days, {weeks} weeks and {months} months left to live.")
