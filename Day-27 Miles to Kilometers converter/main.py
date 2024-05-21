from tkinter import *

FONT = "Arial", 14


def miles_to_km():
    miles = float(input.get())
    km = round((miles * 1.60934), 2)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Labels
label1 = Label(text="Miles", font=FONT)
label1.grid(column=2, row=0)

label2 = Label(text="is equal to", font=FONT)
label2.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

# Button
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

window.mainloop()
