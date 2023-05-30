import turtle
def draw_side ():
    turtle.forward(100)
def turn_right_corner ():
    turtle.right(90)
def turn_star_corner ():
    turtle.right(144)
def draw_square ():
    draw_side()
    turn_right_corner()
    draw_side()
    turn_right_corner()
    draw_side()
    turn_right_corner()
    draw_side()
draw_square()

def draw_star():
    draw_side()
    turn_star_corner()
    draw_side()
    turn_star_corner()
    draw_side()
    turn_star_corner()
    draw_side()
    turn_star_corner()
    draw_side()
    turn_star_corner()
draw_star()
