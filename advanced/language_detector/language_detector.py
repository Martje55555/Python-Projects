# Import the required libraries
from langdetect import detect
from tkinter import *
import tkinter as tk

# Create an instance of tkinter frame or windowdow
window=Tk()

# Set the size of the tkinter windowdow
window.geometry("600x400")
head=Label(window, text="Language Detector", font=('Calibri 15'))
head.pack(pady=20)

def check_language():
    new_text = text.get()
    lang = detect(str(new_text))
    Label(window, text=lang, font=('Calibri 15')).place(x=260,y=200)

text = tk.StringVar()

Entry(window, textvariable=text).place(x=200,y=80,height=30,width=280)# enter a sentence
#create a button
Button(window, text="Check Language",command=check_language).place(x=285,y=150)

window.mainloop()#main command
