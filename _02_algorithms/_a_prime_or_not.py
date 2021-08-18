"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num = simpledialog.askinteger(None, "Insert a number")
    stage = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:

                stage = True

                break
    if stage:
        messagebox.showinfo(None, message="This number is not prime")
    else:
        messagebox.showinfo(None, message="This number is prime")
    # TODO)
    #  1. Ask the user for a number
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    pass
