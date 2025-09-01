from tkinter import *


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles_text_box = Entry(width=10)
miles_text_box.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(row=1, column=0)

converted_km_label = Label(text="0")
converted_km_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

def convert_miles_to_km():
    miles = float(miles_text_box.get())
    km = round(miles * 1.60, 2)
    converted_km_label.config(text=km)

calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()


