from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 8
timer = None

def reset():
    global REPS, timer
    if timer:
        window.after_cancel(timer)
        timer = None

    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    REPS = 8

def countdown(count):
    global timer, REPS
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        if REPS % 2 == 1:
            current_ticks = check_label.cget("text")
            check_label.config(text=current_ticks + "✔️")
        if REPS == 0:
            timer_label.config(text="Timer", fg=GREEN)
            canvas.itemconfig(timer_text, text="00:00")
            check_label.config(text="")
            return
        start()


def start():
    global REPS
    REPS -= 1
    if REPS % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=RED)
    elif REPS % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomatoImg)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
timer_label = Label(text="Timer", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_btn = Button(text="Start", highlightthickness=0, bd=0, command=start)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, bd=0, command=reset)
reset_btn.grid(column=2, row=2)

check_label = Label(text="", font=(FONT_NAME,15), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()