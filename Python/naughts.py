import tkinter as tk
from PIL import ImageTk, Image

#colors w script
bg_color = '#FFF'
text_color = 'Black'

#window
window = tk.Tk()
window.geometry('600x600')
window.title('Naughts and Crosses')
window['background'] = bg_color

title = tk.Label(text = 'Naughts and Crosses',
                        fg = text_color,
                        bg = bg_color)
title.config(font = ('Comic Sans', 20))
title.pack(pady=(50,30))



window.mainloop()