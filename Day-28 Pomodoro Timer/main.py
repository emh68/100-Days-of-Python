from tkinter import *
import math
import pygame.mixer

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#eb1c1c"
# "#e7305b"
GREEN = "#4CBB17"
ORANGE = "#FFB025"
YELLOW = "#f7f5dd"
BLUE = "#7EC8E3"
NAVY_BLUE = "#000C66"
FONT_NAME = "Counter-Strike"
WORK_MIN = 60
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- PLAY SOUND --------------------------------- #
def play():
    pygame.mixer.init()
    pygame.mixer.music.load("angelic_welcome.wav")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1.0)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(fg=BLUE, text="Timer")
    checkmarks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # print(reps)
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(fg=GREEN, text="Break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(fg=ORANGE, text="Break")
    else:
        count_down(work_sec)
        timer_label.config(fg=RED, text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 1:
        count_min = "  "
    if count < 1:
        play()

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
timer_label = Label(fg=BLUE, bg=YELLOW, text="Timer", font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

# Checkmark Label
checkmarks = Label(fg=RED, bg=YELLOW)
checkmarks.grid(column=1, row=5)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

# Start Button
start = Button(text="Start", command=start_timer)
start.grid(column=0, row=4)

# Reset Button
reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=4)

window.mainloop()
