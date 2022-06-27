from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break


def actual_time():
    set_alarm_timer = f"{hour.get()}:{minute.get()}:{seconds.get()}"
    alarm(set_alarm_timer)


clock = Tk()
clock.title(" Alarm Clock")
clock.geometry("400x200")

time_format = Label(clock, text="Enter time in 24 hour format!", fg="red", bg="black",
                    font="Arial")
time_format.pack(side="bottom")

addTime = Label(clock, text="Hour  Min   Sec", font=60)  # .place(x=110)
addTime.pack()

setYourAlarm = Label(clock, text="When to wake you up", fg="blue", relief="solid",
                     font=("Helevetica", 7, "bold"))  # .place(x=0, y=29)
setYourAlarm.pack()

hour = StringVar()
minute = StringVar()
seconds = StringVar()

hourTime = Entry(clock, textvariable=hour, bg="pink", width=15)  # .place(x=110, y=30)
hourTime.pack(side="left")
minuteTime = Entry(clock, textvariable=minute, bg="pink", width=15)  # .place(x=150, y=30)
minuteTime.pack(side="left")
secondsTime = Entry(clock, textvariable=seconds, bg="pink", width=15)  # .place(x=200, y=30)
secondsTime.pack(side="left")

submit = Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time)  # .place(x=110, y=70)
submit.pack()

clock.mainloop()
