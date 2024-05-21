from tkinter import *
import pandas
import random
from time import time

# ------------------------------------ CONSTANTS --------------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
BLACK = "#000000"
FONT = "Arial"
# timer = None
# TIME = 3
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = pandas.DataFrame.to_dict(data, orient="records")


# ------------------------------------ GET WORD ----------------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill=BLACK)
    canvas.itemconfig(card_word, text=current_card["French"], fill=BLACK)
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, card_flip)


# ------------------------------------ REMOVE KNOWN WORDS ------------------------------------------ #
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
    print(len(to_learn))

# ------------------------------------ TIMER ------------------------------------------ #
# def count_down():
#     global timer
#     window.after(3000, card_flip)
#     # canvas.itemconfig(timer_text, text=f"{TIME}")
#     # canvas.itemconfig(timer_text, text=f"{TIME}")
#     # if count == 0:
# count_down()
# if timer == 0:
#     canvas.itemconfig(canvas_image, image=card_back_img)
# if canvas_image == card_front_img:
# window.after(3000, )

# --------------------------------------- CARD FLIP ------------------------------------ #
def card_flip():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill=WHITE, font=(FONT, 30, "italic"))
    canvas.itemconfig(card_word, text=(current_card["English"]), fill=WHITE, font=(FONT, 60, "bold"))


# ----------------------------------------- UI SETUP ------------------------------------
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, card_flip)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 30, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
timer_text = canvas.create_text(400, 380, text="", fill=BLACK, font=("Arial", 30, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button Wrong
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, bd=0, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

# Button Right
check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, bd=0, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
