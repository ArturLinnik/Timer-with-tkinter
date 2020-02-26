
# Creates a timer using the Tkinter GUI

from tkinter import *

def start_timer():
    global hours, minutes, seconds
    seconds -= 1
    label["text"] = "{}:{}:{}".format(hours,
        minutes, seconds)
    if seconds == 0:
        seconds = 60
        minutes -= 1
    elif hours == 0 and minutes == 0 and seconds == 0:
        hours = 0
        minutes = 0
        seconds = 0
    root.after(1000, start_timer)

def entry_text():
    entryText3.set(1)

root = Tk()

hours = 0
minutes = 59
seconds = 60

# Label that shows the timer.
label = Label(root, text="01:00:00")
label.grid(row = 1, column = 1)

# Button for starting the timer.
button = Button(root, text="Start timer", command=start_timer)
button.grid(row = 2, column = 1)

# Entries for the timer's configuration.
entryText1 = StringVar()
entry = Entry(root, textvariable=entryText1)
entry.grid(row = 0, column = 0)

entryText2 = StringVar()
entry2 = Entry(root)
entry2.grid(row = 0, column = 1)

entryText3 = StringVar()
entry3 = Entry(root, textvariable=entryText3)
entry3.grid(row = 0, column = 2)

# Keyboard of numbers.
key_button1 = Button(root, text="1", command=entry_text)
key_button1.grid(row = 3, column = 0)

key_button2 = Button(root, text="2", command=start_timer)
key_button2.grid(row = 3, column = 1)

key_button3 = Button(root, text="3", command=start_timer)
key_button3.grid(row = 3, column = 2)

key_button4 = Button(root, text="4", command=start_timer)
key_button4.grid(row = 4, column = 0)

key_button5 = Button(root, text="5", command=start_timer)
key_button5.grid(row = 4, column = 1)

key_button6 = Button(root, text="6", command=start_timer)
key_button6.grid(row = 4, column = 2)

key_button7 = Button(root, text="7", command=start_timer)
key_button7.grid(row = 5, column = 0)

key_button8 = Button(root, text="8", command=start_timer)
key_button8.grid(row = 5, column = 1)

key_button9 = Button(root, text="9", command=start_timer)
key_button9.grid(row = 5, column = 2)

key_button0 = Button(root, text="0", command=start_timer)
key_button0.grid(row = 6, column = 1)

root.mainloop()
