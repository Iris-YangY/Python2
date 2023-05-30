import turtle
def draw_equilateral (direction, side_length):
    # sig : str , int -> NoneType
    if direction=="R":
        turtle.right(60)
        turtle.forward(side_length)
        turtle.right(120)
        turtle.forward(side_length)
        turtle.right(120)
        turtle.forward(side_length)
    elif direction=="L":
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)
"""direction=input("Enter a direction: ")
side_length=int(input("What is the length? "))"""
draw_equilateral("L",100)
