import turtle
import time
import random

the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]
centralpoint=[(-50,150),(50,150),(150,150),
              (-50,50),(50,50),(150,50),
              (-50,-50),(50,-50),(150,-50)]

def draw_X(pointx, pointy):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(pointx,pointy)
    turtle.pendown()
    turtle.pensize(5)
    turtle.color("red")
    turtle.left(45)
    turtle.forward(45)
    turtle.left(180)
    turtle.forward(90)
    turtle.left(180)
    turtle.forward(45)
    turtle.left(90)
    turtle.forward(45)
    turtle.left(180)
    turtle.forward(90)

def draw_O(pointx, pointy):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(pointx-30,pointy-30)
    turtle.pendown()
    turtle.pensize(5)
    turtle.color("blue")
    turtle.circle(45)

def draw_board(board):
    turtle.clear()
    turtle.tracer(0,0)
    turtle.up()
    turtle.goto(-100,-100)
    turtle.down()
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.up()
    turtle.goto(-100,0)
    turtle.down()
    turtle.forward(300)
    turtle.up()
    turtle.goto(-100,100)
    turtle.down()
    turtle.forward(300)
    turtle.left(90)
    turtle.up()
    turtle.goto(0,-100)
    turtle.down()
    turtle.forward(300)
    turtle.up()
    turtle.goto(100,-100)
    turtle.down()
    turtle.forward(300)
    for i in range(8):
        if the_board[i]=="O":
            draw_O(centralpoint[i][0],centralpoint[i][1])
        elif the_board[i]=="X":
            draw_X(centralpoint[i][0],centralpoint[i][1])
    turtle.update()

def do_user_move(board, x, y):
    print("user clicked at "+str(x)+","+str(y))
    if check_game_over(board)==False:
        index=-1
        return False
    if -100<x<0 and 100<y<200:
        index=0
    elif -100<x<0 and 0<y<100:
        index=3
    elif -100<x<0 and -100<y<0:
        index=6
    elif 0<x<100 and 100<y<200:
        index=1
    elif 0<x<100 and 0<y<100:
        index=4
    elif 0<x<100 and -100<y<0:
        index=7
    elif 100<x<200 and 100<y<200:
        index=2
    elif 100<x<200 and 0<y<100:
        index=5
    elif 100<x<200 and -100<y<0:
        index=8
    if index!=-1:
        if the_board[index]=="_":
            the_board[index]=="O"
        return True
    return False

