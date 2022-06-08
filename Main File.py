"""This program is so we know where camps are overnight
Need to ensure that the quit subroutine is added along with the main function which
needs to be called.
Then create the labels and buttons"""

from tkinter import *
from tkinter import messagebox


# quit subroutine
def quit():
    mw.destroy()

def delrow():
    ()

# start the program running
def main():
    global mw
    mw = Tk()
    mw.title("Julies Party")
    mw.geometry("800x800")
    mw.mainloop()


main()
