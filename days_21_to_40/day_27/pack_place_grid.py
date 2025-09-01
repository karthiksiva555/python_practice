from tkinter import *

window = Tk()
window.title("Pack Place Grid")
window.minsize(height=400, width=400)
window.config(padx=20, pady=20)

label = Label(text="Place Me")
label.config(padx=15, pady=15)
# label.pack(side="left")
# label.place(x=0, y=0)
label.grid(row=0, column=0)

button = Button(text="Submit")
# button.pack(side="right")
# button.place(x=100, y=200)
button.grid(row=2, column=1)

text_box = Entry()
# text_box.pack(side="left")
# text_box.place(x=300, y=250)
text_box.grid(row=1, column=2)


window.mainloop()
