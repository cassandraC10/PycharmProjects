from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    # message_string = strftime("Good Morning Sandra")
    # message_label.config(text=message_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%b %m %y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()
window.title("Cassandra Clock")
time_label = Label(window, font=("consolas", 50), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(window, font=("consolas", 25))
day_label.pack()

date_label = Label(window, font=("consolas", 30))
date_label.pack()

message_label = Label(window, font=("consolas", 20))
message_label.pack()

update()

window = mainloop()
