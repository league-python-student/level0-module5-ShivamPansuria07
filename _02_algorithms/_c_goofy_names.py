"""
Write an algorithm to change a string into a "goofy" version.
"""
import random
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    name = simpledialog.askstring(None, "What is your name?")
    goofy = ""
    for i in range(len(name)):
        randnum = random.randint(0, 2)
        if randnum == 1:
            goofy += name[i].upper()
        else:
            goofy += name[i].lower()
    messagebox.showinfo(None, message=goofy)
    # TODO)
    #  1. Ask the user to enter their name.
    #  2. Use a loop to alternately modify each character of the name into
    #     uppercase and lowercase letters until a new "goofy" representation
    #     of their name has been constructed.
    #     For example, if they enter their name as Alexander Hamilton
    #     their goofy name will be AlExAnDeR HaMiLtOn
    #  3. Show the user the goofy version of their name in a pop-up.
    pass
