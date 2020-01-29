# A starter program for Python with Tkinter
from tkinter import * # import Tkinter library
window = Tk()         # Create the application window

# Add a label with the text "Hello"
lbl = Label(window, text="Xavier Wright", font=("Arial Bold", 50))
lbl2 = Label(window, text= "Hello This is a label", front=("Arial Bold",30))
# Place the label in the window at 0, 0
lbl.grid(column=0, row=1)
lbl2.grid(column=0, row=2)
txt = Entry(window,width=10)
 
txt.grid(column=1, row=0)

window.mainloop()     # Keep the window open
