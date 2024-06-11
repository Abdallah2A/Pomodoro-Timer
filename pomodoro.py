import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    check_label.config(text="")
    timer_label.config(text="Timer")
    global reps
    reps = 0
    
def count_down(time):
    minutes = math.floor(time / 60)
    seconds = math.floor(time % 60)
    
    canvas.itemconfig(timer_text, text= f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
    if time > 0:
        global timer
        timer = window.after(1000, count_down, time-1)
    else:
        start_timer()
        check = ""
        global reps
        for i in range(math.floor(reps / 2)):
            check += "♥ " 
            check_label.config(text= f"{check}")
        
def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg= GREEN)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg= RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg= PINK)

    

window = Tk()
window.title("Pomodoro")
window.config(padx= 150, pady= 100, bg= YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg= YELLOW, fg= GREEN)
timer_label.grid(column= 1, row= 0)

canvas = Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness=0)
image = PhotoImage(file="data/tomato.png")
canvas.create_image(100, 112, image= image)
timer_text = canvas.create_text(103, 130, text="00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column= 1, row= 1)

start_button = Button(text= "Start", font=(FONT_NAME, 10, "bold"), fg= GREEN, highlightthickness= 0, command= start_timer)
start_button.grid(column= 0, row= 2)

reset_button = Button(text= "reset", font=(FONT_NAME, 10, "bold"), fg= RED, highlightthickness= 0, command= reset_timer)
reset_button.grid(column= 2, row= 2)

check_label = Label(text="", font=(FONT_NAME, 15, "bold"), bg= YELLOW, fg= RED)
check_label.grid(column= 1, row= 3)

window.mainloop()