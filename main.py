# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window

score = 0

def addToScore():
  message = txt.get()
  if message == "Jon":
    lbl['text'] = "go away"
  else:
    lbl['text'] = "hello"

# Add a label with the text "Hello"
lbl = Label(window, text=score, font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

btn = Button(window, text="Click", command=addToScore)
btn.grid(column = 0 , row = 1)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)



window.mainloop()     # Keep the window open


