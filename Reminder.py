from tkinter import TkVersion, Button
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


window = Tk
window.title ("Напоминание")
label = Label(text="Установите напоминание", font="Arial", 14)
label.pack(pady=10)
set_button = Button(text="Установить напоминание", command=set)
set_button.pack(pady=10)

window.mainloop()
