# Masibulele Kona
from tkinter import *

myspace = Tk()

myspace.geometry("700x500") # Frame(widthxheight)
myspace.title("My Space")

# Declare widgets
# Lists
weight_kg = Label(myspace, text = "Weight(kg):")
height_cm = Label(myspace, text = "Height(cm):")
gender = Label(myspace, text = "Gender:")
age = Label(myspace, text = "Age:")

# Entry
weight_entry = Entry(myspace, textvariable="")
height_entry = Entry(myspace, textvariable="")
age_entry = Entry(myspace, textvariable="")
bmi_entry = Entry(myspace, textvariable="", state=DISABLED) # It's an Entry but we won't be entering anything, but getting answers.
ibmi_entry = Entry(myspace, textvariable="", state=DISABLED)

# Button
bmi_btn = Button(myspace, text = "BMI")
ibmi_btn = Button(myspace, text = "IBMI")
clear_btn = Button(myspace, text = "Clear")
exit_btn = Button(myspace, text = "Exit")

# Radiobutton
# male_radio_btn = Radiobutton(myspace, text = "Male", variable = "")
# female_radio_btn = Radiobutton(myspace, text = "Female", variable = "")

# Placing the widgets
# Lists
weight_kg.place(x=80, y=30)
height_cm.place(x=370, y=30)
gender.place(x=80, y=90)
age.place(x=418, y=90)

# Entry
weight_entry.place(x=160,y=30)
height_entry.place(x=450,y=30)
age_entry.place(x=450,y=90)
bmi_entry.place(x=150,y=230)
ibmi_entry.place(x=390,y=230)
# Button
bmi_btn.place(x=190,y=170)
ibmi_btn.place(x=450,y=170)
clear_btn.place(x=300,y=300)
exit_btn.place(x=300,y=350)

# Radiobutton
# male_radio_btn(x=10,y=270)
# female_radio_btn(x=10,y=300)

myspace.mainloop()