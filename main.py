from tkinter import *

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 20

# TIMER RESET

# TIMER MECHANISM

# COUNTDOWN MECHANISM

# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="#ffffff")

title_label = Label(text="Timer", fg=GREEN, bg="#000000",
                    font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=860, height=619, bg="#ffffff")
tomato = PhotoImage(file="tomato.png")
canvas.create_image(430, 305, image=tomato)
canvas.create_text(430, 340, text="00:00", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

start_button = Button(text="Start")
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

check_mark = Label(text="✓", fg=GREEN, bg="#000000")
check_mark.grid(column=1, row=3)


window.mainloop()
