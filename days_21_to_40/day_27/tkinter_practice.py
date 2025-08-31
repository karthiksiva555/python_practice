from tkinter import *


window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

# Create GUI components here

#label
label = Label(text="Title", font=("Arial", 24, "bold"))
label.pack()

# Edit a property of an already created widget
# label["text"] = "I am a new Label"
# label.config(text="I am another label")

def button_clicked():
    # print("button clicked")
    # label.config(text="Button got clicked!")
    label.config(text=text_box.get())

text_box = Entry()
text_box.pack()
text_box.insert(END, "Placeholder text")
# use text_box.get() to get the value entered in the text box

button = Button(text="Update Title", command=button_clicked)
button.pack()

# Text
multi_line_box = Text(height=5, width=30)
multi_line_box.focus()
multi_line_box.insert(END, "Multi line text box example \n with text spanned in multiple lines")
print(multi_line_box.get("1.0", END)) # gets text from line 1, char 0 till the END
multi_line_box.pack()

# Spin Box
def spin_box_used():
    print(spin_box.get())

spin_box = Spinbox(from_=0, to=10, width=5, command=spin_box_used)
spin_box.pack()

# Scale
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=5, command=scale_used)
scale.pack()

# Check box
def checkbox_used():
    print(check_box_state.get())

check_box_state = IntVar()
check_button = Checkbutton(text = "I agree to the terms and conditions",
                           variable= check_box_state, command=checkbox_used)
check_button.pack()

# Radio Button
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
option_1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
option_2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
option_1.pack()
option_2.pack()

# List Box
def list_box_used(event):
    print(list_box.get(list_box.curselection()))

list_box = Listbox(height=4)
fruits = ["Apple", "Banana", "Cherry", "Dragon Fruit"]
for fruit in fruits:
    list_box.insert(fruits.index(fruit), fruit)
list_box.bind("<<ListboxSelect>>", list_box_used)
list_box.pack()

window.mainloop() # to keep the window open