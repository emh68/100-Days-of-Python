# from tkinter import *
#
# top = Tk()
# top.geometry("700x300")
# top.title("StringVar Object in Entry Widget")
#
# var = StringVar(top)
#
# def submit():
#    Label2.config(text="Your User ID is: " +var.get(), font=("Calibri,15,Bold"))
#
# Label1 = Label(top, text='Your User ID:')
# Label1.grid(column=0, row=0, padx=(20,20), pady=(20,20))
#
# myEntry = Entry(top, textvariable=var)
# myEntry.grid(column=1, row=0, padx=(20,20), pady=(20,20))
#
# myButton = Button(top, text="Submit", command=submit)
# myButton.grid(column=2, row=0)
#
# Label2 = Label(top, font="Calibri,10")
# Label2.grid(column=0, row=1, columnspan=3)
#
# top.mainloop()

# fruits = ["Apple", "Pear", "Orange"]
#
#
# # TODO: Catch the exception and make sure the code runs without crashing.
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass


print(total_likes)
