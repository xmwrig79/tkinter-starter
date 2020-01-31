# A starter program for Python with Tkinter
from tkinter import * # import Tkinter library
from tkinter import ttk

window = Tk()         # Create the application window

# Add a label with the text "Hello"
lbl = Label(window, text="Xavier Wright", font=("Arial Bold", 50))
lbl2 = Label(window, text="Hello This is a label", font=("Arial Bold",30))
# Place the label in the window at 0, 0
lbl.grid(column=0, row=1)
lbl2.grid(column=0, row=2)
txt = Entry(window,width=10)
txt.grid(column=3, row=0)
 
btn = Button(window, text="Click Me")
 
btn.grid(column=0, row=5)
btn = Button(window, text="This is a button")
 
btn.grid(column=0, row=9)
rad1 = Radiobutton(window,text='First', value=1)
 
rad2 = Radiobutton(window,text='Second', value=2) 
 
rad3 = Radiobutton(window,text='Third', value=3)
 
rad1.grid(column=0, row=0)
 
rad2.grid(column=1, row=0)
 
rad3.grid(column=2, row=0)
 
btn.grid(column=3, row=0)
 
from tkinter.ttk import Progressbar
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
 
bar['value'] = 70
 
bar.grid(column=12, row=0)

from tkinter import Menu

menu = Menu(window)
new_item =Menu(menu)
 
new_item.add_command(label='New')
 
menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)

l1 = Label(text="This is my theme", fg="white", bg="blue")
l1.grid(column=20, row=20)
#l2 = tkinter.Label(text="Test", fg="black", bg="white")
# style = ttk.Style()

# style.configure(BW.TLablel", foreground= "black, background="white")

window.mainloop()     # Keep the window open
x = ____
y = 23

if x > 50:
  x = 5
  if y < 20:
    x = 3
else:
  x = 2
  y = 10

print(x + y)