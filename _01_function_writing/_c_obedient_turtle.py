"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle


if __name__ == '__main__':
    # TODO)

    window = turtle.Screen()
    window.bgcolor('white')

    #   1. Create a turtle.
    Shivam = turtle.Turtle()
    Shivam.shape('turtle')
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    def square():
        for i in range(1, 5):
            Shivam.speed(2)
            Shivam.pendown()
            Shivam.forward(100)
            Shivam.right(90)

    def triangle():
        for i in range(0, 3):
                Shivam.speed(2)
                Shivam.pendown()
                Shivam.left(120)
                Shivam.forward(100)


    def hexagon():
            Shivam.penup()
            Shivam.forward(50)
            Shivam.pendown()
            Shivam.right(60)
            Shivam.forward(50)
            Shivam.right(60)
            Shivam.forward(50)
            Shivam.right(60)
            Shivam.forward(50)
            Shivam.right(60)
            Shivam.forward(50)
            Shivam.right(60)
            Shivam.forward(50)
            Shivam.right(60)
            Shivam.forward(50)


    #   3. Ask the user for the for a shape to draw.
    str = simpledialog.askstring(None, "What shape do you want to draw?")
    if str=="square":
        square()
    elif str == "triangle":
        triangle()
    else:
        hexagon()
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    pass
