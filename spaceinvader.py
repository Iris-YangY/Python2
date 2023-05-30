# CS-UY 1114
# Final project

import turtle
import time

# This variable store the horizontal position
# of the player's ship. It will be adjusted
# when the user press left and right keys, and
# will be used by the draw_frame() function to draw
# the ship. The ship never moves vertically, so
# we don't need a variable to store its y position.
userx = 0

# This variable is a list of enemies currently in
# the game. Each enemy is represented by a tuple
# containing its x,y position as well as a string
# indicated the enemy's current direction of travel
# (either left or right). 
# Your final game should include more enemies, although
# the exact arrangement is up to you.
enemies = [(300,50, "left"), (400,50, "left"), (350, -50, "right")]

# This variable is a list of all bullets currently
# in the game. It is a list of tuples of (x,y)
# coordinates, one for each bullet. An elements will
# be added when a new bullet is fired, and removed
# when a bullet is destroyed (either by leaving
# the screen or by hitting an enemy).
bullets = []

# This variable is checked by the game's main
# loop to determine when it should end. When
# the game ends (either when the player's ship
# is destroyed, or when all enemies have been 
# destroyed), your code should set this variable
# to True, causing the main loop to end.
gameover = False

def draw_frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables, draw all visual
    elements on the screen: the player's ship,
    the enemies, and the bullets.
    Please note that this is your only function
    where drawing should happen (i.e. the only
    function where you call functions in the
    turtle module). Other functions in this
    program merely update the state of global
    variables.
    This function also should not modify any
    global variables.
    Hint: write this function first!
    """
    pass # your code here

def key_left():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the player's ship
    appropriately by modifying the variable
    userx.
    """
    global userx
    pass # your code here

def key_right():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the player's ship
    appropriately by modifying the variable
    user1x.
    """
    global userx
    pass # your code here

def key_space():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the space key. It should
    add a new bullet to the list of bullets.
    """
    pass # your code here

def physics():
    """
    signature: () -> NoneType
    Update the state of the game world, as
    stored in the global variables. Here, you
    should check the positions of the bullets,
    and remove them if they go off the screen
    or collide with an enemy. In the later case
    you should also remove the enemy. That is,
    given the current position of the bullets,
    calculate their position in the next frame.
    """
    global bullets
    global enemies
    pass # your code here

def ai():
    """
    signature: () -> NoneType
    Perform the 'artificial intelligence' of
    the game, by updating the position of the
    enemies, storied in the enemies global
    variable. That is, given their current
    position, calculate their position
    in the next frame.
    If the enemies reach the player's ship,
    you should set the gameover variable
    to True. Also, if there are no more
    enemies left, set gameover to True.
    """
    global enemies
    global gameover
    pass # your code here

def reset():
    """
    signature: () -> NoneType
    This function is called when your game starts.
    It should set initial value for all the
    global variables.
    """
    global enemies
    global bullets
    global userx
    global gameover
    pass # your code here

def main():
    """
    signature: () -> NoneType
    Run the game. You shouldn't need to
    modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onkey(key_left, "Left")
    turtle.onkey(key_right, "Right")
    turtle.onkey(key_space, "space")
    turtle.listen()
    reset()
    while not gameover:
        physics()
        ai()
        turtle.clear()
        draw_frame()
        turtle.update()
        time.sleep(0.05)

main()
