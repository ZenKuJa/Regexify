from tkinter import *
import tkinter as tk


window = tk.Tk()
window.geometry("514x802")
window.title("RegEx Generator")
window.config(background="#424242")
window.resizable(False,False)

RegName = Label(window,width=20, height=1, text="RegEx Generator", font=("Irish Grover",22,"bold"),fg="#FFFFFF", bg="#424242" )
RegName.place(relx=0.5, rely=0.02, anchor="n")

canvas = canvas = tk.Canvas(window, width=450, height=650, bg="black", highlightthickness=0)
canvas.place(relx=0.5, rely=0.5, anchor="center")
canvas.place(relx=0.5, rely=0.5, anchor="center")


window.mainloop()


