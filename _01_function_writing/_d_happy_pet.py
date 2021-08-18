"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk

happiness = 0

if __name__ == '__main__':
    num = 0

    def eat():
        messagebox.showinfo(None,message="Your pets happiness has increased!")

    def walk():
        if str == "bird":
            messagebox.showinfo(None,message="Your birds happiness has decreased!")
        elif str == "dog":
            messagebox.showinfo(None,message="Your dogs happiness has increased!")
        elif str == "cat":
            messagebox.showinfo(None,message="Your cats happiness has decreased!")

    def play():
        messagebox.showinfo(None,message="Your pets happiness has increased!")
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    str = simpledialog.askstring(None, "What pet do you want? (bird, dog, cat)")
    # satisfied = simpledialog.askstring(None, "Are you currently satisfied with your birds hapiness?")
    while True:
        str2 = simpledialog.askstring(None, "Do you want your " + str + " to eat, walk, or play?")
        if str2 == "eat":
            eat()
            satisfied = simpledialog.askstring(None, "Are you satisfied with your pets happiness level?")
            if satisfied == "yes":
                break
        elif str2 == "walk":
            walk()
            satisfied = simpledialog.askstring(None, "Are you satisfied with your pets happiness level?")
            if satisfied == "yes":
                break
        elif str2 == "play":
            play()
            satisfied = simpledialog.askstring(None, "Are you satisfied with your pets happiness level?")
            if satisfied == "yes":
                break
        else:
            messagebox.showerror(None, message="Please type one of the following eat, walk, or play")




    # str3 = simpledialog.askstring(None, "Are you satisfied with your " + str + "'s" + " happiness level?")
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!


    pass
