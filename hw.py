# Jiajun Wang
# CS-UY 1114
# 5 March, 2019
# Homework 4

# Problem1
# 1
'''
@
@@@
@@@@@@
@@@@@@@@@@
@@@@@@@@@@@@@@@
'''

# 2
'''
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
'''

# 3
'''
0
03
036
0369
'''
# problem2
def contains_two_fives(n):
    count = 0
    while n > 0:
        if n%10==5:
            count+=1
            n=n//10
        else:
            n=n//10
    if count>=2:
        return True
    else:
        return False


# problem3
def multiples_of_three_while(n):
    count = 0
    while count < n:
        mul = 3 * (count + 1)
        print(mul)
        count += 1


# problem4
def multiples_of_three_for(n):
    for count in range (0,n):
        mul = 3 * (count + 1)
        print(mul)       

# problem5
import turtle
def polygon(size, sides):
    count = 0
    while count < sides:
        turtle.forward(size)
        turtle.left(360/sides)
        count += 1


# problem6
def upper(n):
    count = 0
    blank = 0
    numasterisks=2*n-1
    for count in range (0,n):
        print(blank*" " + numasterisks*"*")
        numasterisks -= 2
        blank += 1
def lower(n):
    count = 0
    blank = n-1
    numasterisks=2*n-1
    for count in range (0,n):
        numasterisks=count*2+1
        print(blank*" " + numasterisks*"*")
        numasterisks += 2
        blank -= 1
def hourglass(n):
    upper(n)
    lower(n)


# problem7
import random
def guessing_game():
    print ("I am thinking of a number between 1 and 100, try to guess it.")
    computer = random.randint(1,100)
    player = input("Please enter a number:")
    if player.isdigit() == False:
        print ("Sorry, but it's not a number between 1 and 100.")
    else:
        if int(player)>computer:
            print ("Your guess was too high, try again.")
        elif int(player)<computer:
            print ("Your guess was too low, try again.")
        else:
            print ("Congratulation, you guessed the number.")
            return
    while True:
        player = input("Please enter a number between 1 and 100:")
        if player.isdigit() == False:
            print ("Sorry, but it's not a number between 1 and 100.")
        else:
            if int(player)>computer:
                print ("Your guess was too high, try again.")
            elif int(player)<computer:
                print ("Your guess was too low, try again.")
            else:
                print ("Congratulation, you guessed the number.")
                break


# problem8
import math
def mul_table():
    for i in range(1, 6):
        for j in range(1,11):
            print (j**i, "\t",end="")
        print()


