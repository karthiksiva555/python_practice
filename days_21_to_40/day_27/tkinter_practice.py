from tkinter import *


window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

# Create GUI components here

#label
label = Label(text="I am a Label", font=("Arial", 24, "bold"))
label.pack()

label["text"] = "I am a new Label"
label.config(text="I am another label")

def button_clicked():
    print("button clicked")

button = Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop() # to keep the window open