# Import the required libraries
import urllib.request
from tkinter import *
import tkinter as tk

# Create an instance of tkinter frame or windowdow
window=Tk()

# Set the size of the tkinter windowdow
window.geometry("600x400")
#window.title("Website Connectivity Checker")#give title to the window
head=Label(window, text="Website Connectivity Checker", font=('Calibri 15'))# a lable
head.pack(pady=20)

#fucntion to check
def check():
    web= (url.get())
    status_code = urllib.request.urlopen(web).getcode()
    website_is_up = status_code == 200
    if website_is_up==TRUE:
        Label(window, text="Website Available", font=('Calibri 15')).place(x=260,y=200)
    else:
        Label(window, text="Website Not Available", font=('Calibri 15')).place(x=260,y=200)


url=tk.StringVar()# url is of string type
Entry(window, textvariable=url).place(x=200,y=80,height=30,width=280)# enter a website url
#create a button
Button(window, text="Check",command=check).place(x=285,y=150)

window.mainloop()#main command
