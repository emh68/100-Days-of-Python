import time

# Greeting
print("Welcome to the Band Name Generator.")


time.sleep(1)
# Prompt user for the city that they grew up in.
city = input("What city did you grow up in? \n")

# Prompt user for the name of a pet.
pet = input("What is the name of a pet you have owned? \n")

# Combine the name of their city and pet and show them their band name.
band_name = city + " " + pet
print("Your band name could be " + band_name)
