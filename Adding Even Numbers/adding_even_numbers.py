# This code adds all of the even numbers from 0 to the number the user inputs
target = int(input("Enter a number between 0 and 1000: "))

total = 0
for number in range(0, target + 1, 2):
    total += number
print(total)
