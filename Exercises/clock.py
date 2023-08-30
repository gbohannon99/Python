from tkinter import *
from time import *

#Function sets the day and time for the respective Labels
#   and updates the window every 1000 miliseconds (1second)
def update():
    time_string = strftime("%I:%M:%S %p")
    time_Label.config(text=time_string)

    day_string = strftime("%A")
    day_Label.config(text=day_string)

    date_string = strftime("%B %d ,%Y")
    date_Label.config(text=date_string)

    time_Label.after(1000, update)


window = Tk()
window.configure(background="Black")

#Creates a Label for the Time
time_Label = Label(window,
                   font=("Arial", 45),
                   fg="Green",
                   bg="Black")
time_Label.pack()

#Creates a Label for the Day of the Week
day_Label = Label(window,
                   font=("Arial", 15),
                   fg="Green",
                   bg="Black")
day_Label.pack()

#Creates a Label for the Date
date_Label = Label(window,
                   font=("Arial", 20),
                   fg="Green",
                   bg="Black")
date_Label.pack()

#Call the Update Function to set the day and time
update()


window.mainloop()