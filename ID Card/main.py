# ID Badge Generator

print("Please enter the following information \n")

first_name = input("What is your first name? ").capitalize()
last_name = input("What is your last name? ").upper()
email = input("Please enter your email address: ")
phone = input("Please enter your phone number: ")
job_title = input("What is your job title? ").title()
ID_number = input("Please enter your ID number if you have one: ")

print("The ID Card is: ")
print("______________________________")
print(f"{last_name}, {first_name}")
print(job_title)
print(f"ID: {ID_number} \n")
print(email)
print(phone + " \n")
print("------------------------------")