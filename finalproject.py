# CS-UY 1114
# Final project
# Yadi Yang

import turtle
import time
import random

# This list represents the state of the
# board. It's a list of nine strings,
# each of which is either "X", "O", "_",
# representing, respectively,
# a position occupied by an X, by an O, and
# an unoccupied position. The first three
# elements in the list represent the first row,
# and so on. Initially, all positions are
# unoccupied.
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
    turtle.left(45)
    turtle.pensize(1)
    turtle.color("black")

def draw_O(pointx, pointy):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(pointx,pointy-45)
    turtle.pendown()
    turtle.pensize(5)
    turtle.color("blue")
    turtle.circle(45)
    turtle.pensize(1)
    turtle.color("black")
    
def draw_board(board):
    """
    signature: list(str) -> NoneType
    The current state of the board, indicating
    the position of all pieces, is given
    as a parameter. This function should draw
    the entire board on the screen using turtle.
    It must draw the grid lines as well as
    the X and O pieces at the position
    indicated by the parameter.
    Hint: Write this function first!
    """
    turtle.clear()
    turtle.tracer(0,0)
    turtle.up()
    turtle.goto(-100,-100)
    turtle.down()
    for i in range(4):
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
    turtle.right(90)
    for i in range(9):
        if board[i]=="O":
            draw_O(centralpoint[i][0],centralpoint[i][1])
        elif board[i]=="X":
            draw_X(centralpoint[i][0],centralpoint[i][1])
    turtle.update()
          
def do_user_move(board, x, y):
    """
    signature: list(str), int, int -> bool
    The current state of the board is given as
    a parameter, as well as the x,y screen coordinate
    indicating where the user clicked. This function
    should update the board state variable
    with an O in the corresponding position. Your
    code will need to translate the screen coordinate
    (a pixel position where the user clicked) into the
    corresponding board position (a value between 0 and
    8 inclusive, identifying one of the 9 board positions).
    The function returns a bool, indicating if
    the operation was successful: if the user
    clicks on a position that is already occupied
    or outside of the board area, the move is
    invalid, and the function should return False,
    otherise True. user have o move, computer have x move
    """
    print("user clicked at "+str(x)+","+str(y))
    if check_game_over(board)==True:
        index=-1
    elif -100<x<0 and 100<y<200:
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
    else:
        index=-1
    if index!=-1:
        if board[index]=="_":
            board[index]="O"
            return True
        return False

def check_game_over(board):
    """
    signature: list(str) -> bool
    Given the current state of the board, determine
    if the game is over, by checking for
    a three-in-a-row pattern in horizontal,
    vertical, or diagonal lines; and also if the
    game has reached a stalemate, achieved when
    the board is full and no further move is possible.
    If there is a winner or if there is a stalemante, display
    an appropriate message to the user and clear the board
    in preparation for the next round. If the game is over,
    return True, otherwise False.
    """
    # your code here
    over=['012','345','678','036','147','258','048','246']
    gameover=False
    userwin=False
    stalemate=False
    for check in over:
        result=''
        for move in check:
            result+=board[int(move)]
        if result=="OOO":
            userwin=True
            gameover=True
        elif result=="XXX":
            gameover=True
    if not "_" in board:
        stalemate=True
        gameover=True
    if gameover:
        global the_board
        the_board=[ "_", "_", "_",
                    "_", "_", "_",
                    "_", "_", "_"]
        turtle.up()
        turtle.goto(-80,-200)
        turtle.down()
        turtle.color('lightyellow')
        turtle.pensize(180)
        turtle.forward(260)
        turtle.up()
        turtle.color('black')
        turtle.pensize(1)
        turtle.up()
        turtle.goto(-90,-250)
        turtle.down()
        if userwin:
            turtle.write("You Win!", font=("Times New Roman", 60, "bold"))
        elif stalemate:
            turtle.write("Stalemate", font=("Times New Roman", 60, "bold"))
        else:
            turtle.write("Computer\n    Win!", font=("Times New Roman", 60, "bold"))
        turtle.up()
        turtle.goto(0,-270)
        turtle.down()
        turtle.color("darkred")
        turtle.write("Play again", font=("Times New Roman", 20, "bold"))
        turtle.up()
        turtle.color('black')
        turtle.pensize(1)
        turtle.down()
    return gameover

def do_computer_move(board):
    """
    signature: list(str) -> NoneType
    Given a list representing the state of the board,
    select a position for the computer's move and
    update the board with an X in an appropriate
    position. The algorithm for selecting the
    computer's move shall be as follows: if it is
    possible for the computer to win in one move,
    it must do so. If the human player is able 
    to win in the next move, the computer must
    try to block it. Otherwise, the computer's
    next move may be any random, valid position
    (selected with the random.randint function).
    """
    computermove=False
    over=['012','345','678','036','147','258','048','246']
    if board[4]=="_":
        board[4]="X"
        computermove=True
    while not computermove:
        nextstepo=[]
        nextstepx=[]
        for check in over:
            line=''
            for move in check:
                if board[int(move)]=="O":
                    line+='O'
                elif board[int(move)]=='X':
                    line+='X'
            if line=='OO':
                nextstepo.append(check)
            elif line=='XX':
                nextstepx.append(check)
                
        if len(nextstepo)>0:
            index=random.randint(0,len(nextstepo)-1)
            position=nextstepo[index]
            for num in position:
                if board[int(num)]=="_":
                    board[int(num)]="X"
                    computermove=True
        elif len(nextstepx)>0:
            index2=random.randint(0,len(nextstepx)-1)
            position2=nextstepx[index2]
            for num2 in position2:
                if board[int(num2)]=="_":
                    board[int(num2)]="X"
                    computermove=True
        else:
            index3=random.randint(0,8)
            if board[index3]=="_":
                board[index3]="X"
                computermove=True
    
def clickhandler(x, y):
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        if not check_game_over(the_board):
            do_computer_move(the_board)
            draw_board(the_board)
            check_game_over(the_board)

def main():
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()

main()
