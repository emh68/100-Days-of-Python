# Calculating Body Mass Index (height / divided by weight squared) using imperial measurements.
# If using metric measurements (i.e. meters and kilograms) remove the * 703

height = int(input("Please enter your height in inches: "))
weight = int(input("Please enter your weight in lbs: "))

result = (weight / height ** 2) * 703
BMI = round(result, 2)
# print(format(BMI,".2f"))
if BMI >= 40:
    print(f"Your BMI is {BMI} and you are very obese.")
elif BMI >= 30 and BMI <= 39:
    print(f"Your BMI is {BMI} and you are obese.")
elif BMI >= 25 and BMI <= 29:
    print(f"Your BMI is {BMI} and you are overweight.")
elif BMI >= 19 and BMI <= 24:
    print(f"Your BMI is {BMI} and you are normal weight.")
else:
    print(f"Your BMI is {BMI} and you are underweight.")
