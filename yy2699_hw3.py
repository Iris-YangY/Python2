# Pat McYadi Yang
# CS - UY 1114
# 17 Feb 2019
# Homework 3

# Problem 1
"""
a) 0
OK
Wow
Done
b) 1
Zoom
Done
c) 6
Wow
Done
d) 8
Zoom
Done
"""

# Problem 2
"""
if doesSignificantWork and makesBreakthrough:
        nobelPrizeCandidate = True
else:
    nobelPrizeCandidate = False

nobelPrizeCandidate = doesSignificantWork + makesBreakthrough
"""

# Problem 3
def call_cost(day, time, length):
    day=str(day)
    time=int(time)
    length=int(length)
    if day=="Sat":
        total=length*0.15
    elif day=="Sun":
        total=length*0.15
    else:
        if time<=800 or time>=1800:
            total=length*0.25
        else:
            total=length*0.4
    return total

# Problem 4
import random
def rock_paper_scissors():
    user=input("Please enter rock, paper, or scissors: ")
    computerselect=random.randint(0,2)
    if computerselect==0:
        computer="rock"
        if user=="paper":
            outputprint=("You win!")
        elif user=="scissors":
            outputprint=("You lose!")
        else:
            outputprint=("No winner")
    elif computerselect==1:
        computer="paper"
        if user=="scissors":
            outputprint=("You win!")
        elif user=="rock":
            outputprint=("You lose!")
        else:
            outputprint=("No winner")
    elif computerselect==2:
        computer="scissors"
        if user=="rock":
            outputprint=("You win!")
        elif user=="paper":
            outputprint=("You lose!")
        else:
            outputprint=("No winner")
    print("Computer selected: ",computer)
    print(outputprint)
#rock_paper_scissors()

# Problem 5
import math
def quadratic(a,b,c):
    if a==0:
        #if b==0 and c!=0:
            #print("This equation has no solution.")
        #elif b==0 and c==0:
           #print("This equation has infinite many solutions.")
        if b!=0:
            x=-c/b
            print("This equotion has a single real solution: ",x)
    if a!=0:
        theta=math.pow(b,2)-4*a*c
        if theta>0:
            x1=(-b+math.sqrt(theta))/2*a
            x2=(-b-math.sqrt(theta))/2*a
            print("This equation has two solutions: x1=",x1,"x2=",x2)
        elif theta==0:
            x=-b/2*a
            print("This equation has a single real solution: ",x)
        #else:
            #print("This equation has no real solution.")
quadratic(0,0,16)
