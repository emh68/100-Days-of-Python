import random

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(",")

num_items = len(names)

random_num = random.randint(0, num_items - 1)

print(f"The person paying for the meal is {names[random_num]}")
