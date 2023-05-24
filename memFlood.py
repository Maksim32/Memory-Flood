# v 1.1

import tkinter as tk
from os import path

# Initializing variables
cycle = 0
words = "you are fucked!!"
size = 0

# Defining the flood function which opens a file called data.txt and writes on it.
def flood(mbs):
    global size
    with open("data.txt", "w") as f:
        for i in range(mbs * 1024):
            for x in range(65536):
                f.write(words)
    print("done!")
    # Calculate the file size in megabytes
    size = path.getsize("data.txt")
    size = size / (1024 ** 2)
    varSizeLabel.config(text=size)  # Update the varSizeLabel with the calculated file size

# This function fetches the value inputted from the user and stores it in a variable
def getUsrCycle(event):
    global cycle
    cycle = int(cycle_textbox.get())
    print(cycle)
    cycle_textbox.delete(0, tk.END)
    startBtn.config(command=lambda: flood(cycle))

# Creating the main window
window = tk.Tk()
window.geometry("230x100")
window.title("Memory hogger")

# Creating and placing GUI elements
megabyteLabel = tk.Label(text="Gigabytes:")
megabyteLabel.grid(column=1, row=1)

cycle_textbox = tk.Entry(window, foreground="white", width=10)
cycle_textbox.grid(column=1, row=2)
cycle_textbox.bind('<Return>', getUsrCycle)

startBtn = tk.Button(window, text="Start Flood", command=lambda: flood(cycle), height=2)
startBtn.grid(column=1, row=3)

showSizeLabel = tk.Label(window, text="True file size (mb):")
showSizeLabel.grid(column=3, row=1)

varSizeLabel = tk.Label(window, text=size)
varSizeLabel.grid(column=3, row=2)

escBtn = tk.Button(window, text="Quit", command=exit)
escBtn.place(x=100, y=50)

# Start the main event loop
window.mainloop()
