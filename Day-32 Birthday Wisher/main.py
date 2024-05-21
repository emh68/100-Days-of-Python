import random
import smtplib
import datetime as dt

with open("quotes.txt") as data_file:
    data = data_file.readlines()
    quotes = random.choice(data)
# print(quotes)

now = dt.datetime.now()
day_of_week = now.weekday()
# print(day_of_week)

if day_of_week == 0:
    my_email = "pepefoofoo@gmail.com"
    password = "oxwabjdotumehgbq"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="emanhacks@yahoo.com",
            msg=f"Subject:Motivational Quotes\n\n{quotes}"
        )

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# if year == 2023:
#     print("Wear a face mask")
#
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1982, month=1, day=30)
# print(date_of_birth)
