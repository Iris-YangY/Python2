# Pat McYadi Yang
# CS - UY 1114
# 17 Feb 2019
# Homework 4

# Problem 1
"""
1.
@
@@@
@@@@@@
@@@@@@@@@@
@@@@@@@@@@@@@@@
2.
1 1
2 2
2 1
3 3
3 2
3 1
4 4
4 3
4 2
4 1
3.
0369
"""
# Problem 2
def contains_two_fives(n):
    """sig: int -> bool
    Give a four-digit positive decimal integer,
    the function will return True if the number
    contains at least two fives, or False otherwise.
    """
    count=0
    while n>0:
        if n%10==5:
            count+=1
        n//=10
    return count>=2

# Problem 3
def multiples_of_three_while(n):
    # sig: int -> NoneType
    count=0
    acc=0
    while count<n:
        count+=1
        acc+=3
        print(acc)
# Problem 4
def multiples_of_three_for(n):
    acc=0
    for i in range(n):
        acc+=3
        print(acc)
# Problem 5
import turtle
def polygon(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360/sides)
# Problem 6
def hourglass(n):
    num=n
    for i in range(n):
        numspaces=i
        numasterisks=2*num-1
        print(numspaces * " " + numasterisks * "*")
        num-=1
    for i in range(1,n+1,1):
        numspaces=n-1
        numasterisks=2*i-1
        n-=1
        print(numspaces * " " + numasterisks * "*")
# Problem 7
import random
def guessing_game():
    guessing=random.randint(1,100)
    print("I'm thinking of a number between 1 and 100, try to guess it.")
    user=input("Please enter a number between 1 and 100:")
    
    while user!=guessing:
        if not user.isdigit():
            print("Sorry, but \"",user,"\" is not a number between 1 and 100.")
            user=input("Please enter a number between 1 and 100:")
        elif int(user)<guessing:
            print("your guess was too low, try again.")
            user=input("Please enter a number between 1 and 100:")
        elif int(user)>guessing:
            print("your guess was too high, try again.")
            user=input("Please enter a number between 1 and 100:")
        elif int(user)==guessing:
            print("Congratulations, you guessed the number!")
            break
# Problem 8
import math
def mul_table():
    output=""
    for i in range(1,6,1):
        for j in range(1,11,1):
            result=str(int(math.pow(j,i)))
            output+=result+"\t"
    print(output)
