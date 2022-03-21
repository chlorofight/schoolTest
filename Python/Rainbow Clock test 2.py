from tkinter import *
import time
import random
#eadfcb
colors = ['e','a','d','f','c','b','1','2','3','4','5','6','7','8','9']
bg_color = ('#' + "".join(random.choices(colors, k = 6)))
fg_color = ('#' + "".join(random.choices(colors, k = 6)))
print(bg_color)
def spam():
    global time1, bg_color, fg_color
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    bg_color = ('#' + "".join(random.choices(colors, k = 6)))
    fg_color = ('#' + "".join(random.choices(colors, k = 6)))
    clock.config(bg=bg_color)
    clock.config(fg=fg_color)
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    
    # calls itself every 200 milliseconds
    clock.after(2, spam)

root = Tk()
time1 = ''
clock = Label(root, font=('times', 20, 'bold'), bg=bg_color)
clock.pack(fill=BOTH, expand=1)
spam()
root.mainloop()