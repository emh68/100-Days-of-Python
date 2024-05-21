from datetime import datetime
import smtplib
import random
import pandas


##################### Normal Starting Project ######################
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
# HINT 2: Use pandas to read the birthdays.csv
# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formatted like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
# Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
# e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
# Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_info = pandas.DataFrame.to_dict(data)
birthdays_dict = {(data_row["month"],  data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        birthday_letter = contents.replace("[NAME]", (birthday_person["name"]))

    my_email = "pepefoofoo@gmail.com"
    password = "oxwabjdotumehgbq"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="emanhacks@yahoo.com",
            msg=f"Subject: Happy Birthday\n\n{birthday_letter}"
        )