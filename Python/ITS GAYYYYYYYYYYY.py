from tkinter import *
import time
import random
#eadfcb
colors = ['green', 'red', 'blue', 'yellow', 'orange', 'purple']
bg_color = random.choice(colors)


def spam():
    global time1, bg_color
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    bg_color = random.choice(colors)
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.config(bg=bg_color)
    clock.after(20, spam)

root = Tk()
time1 = ''
clock = Label(root, font=('times', 20, 'bold'), bg=bg_color)
clock.pack(fill=BOTH, expand=1)
spam()
root.mainloop()