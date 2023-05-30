# CS-UY 1114
# Final project

import turtle
import time

# gravitional constant (to be read from file)
G = 0

# current state of all bodies (to be read from file)
# each entry in the list is a tuple consisting of:
#   body name
#   body position (x,y)
#   body velocity (x,y)
#   body mass
# This value is updated at each step of the simulation
# by the update_positions and update_velocities functions.
# sig: list(tuple(str, float, float, float, float, float))
bodies = [("Sun", 500.0, 500.0, 0.0, 0.0, 100000000.0), 
          ("Splat", 255.0, 255.0, 2.0, 0.0, 1.0)]

def readfile(filename):
    """
    signature: str -> tuple(float, list(tuple(str, float, float, float, float, float)))
    This function is called only once, when your
    program first starts. It should read the file
    named in its argument, which contains the correct value
    of the gravitional constant and the initial
    data about the planets. It should return a tuple
    consisting of two values: the value of the
    gravitational constant G, and a list of all
    the bodies read from the file.
    This function should not modify any global
    variables.
    """
    pass # your code here

def draw_frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables, draw all visual
    elements on the screen: the planets
    and their labels, and their current positions.
    Please note that this is your only function
    where drawing should happen (i.e. the only
    function where you call functions in the
    turtle module). Other functions in this
    program merely update the state of global
    variables.
    This function also should not modify any
    global variables.
    """
    pass # your code here

def update_velocities():
    """
    signature: () -> NoneType
    This function updates the global bodies variable
    with the updated velocities of the bodies, as
    described above.
    That is, given the current velocities and
    positions of each body, calculate their velocity
    at the next frame.
    """
    global bodies
    pass # your code here

def update_positions():
    """
    signature: () -> NoneType
    This function updates the global bodies variable
    with the updated positions of the bodies, as
    described above.
    That is, given the current velocities and
    positions of each body, calculate their position
    at the next frame.
    """
    global bodies
    pass # your code here

def main():
    """
    signature: () -> NoneType
    Run the simulation. You shouldn't
    need to modify this function.
    """
    global G, bodies
    turtle.tracer(0,0)
    turtle.hideturtle()
    (G, bodies) = readfile("bodies.txt")
    while True:
        update_velocities()
        update_positions()
        turtle.clear()
        draw_frame()
        turtle.update()
        time.sleep(0.05)

main()
