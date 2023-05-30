# Problem 1
"""(a)
3
2
1
0

(b)
5
6
7
8
...

(c)
8
4
2
1
0

(d)
2
4
6
8

(e)

x
xx
xxx
xxxx

(f)
10
8
6
4
2
"""

# Problem 2
# (a)
for i in range(1,11,1):
    if i<5 and i!=2:
        print("X")

# (b)
i=1
while i<=10:
    print("X")
    i+=3

# (c)
i=10
while i<100:
    print("X")
    i+=10

# (d)
for i in range(10,2,-1):
    print('X')

# Problem 3
import turtle
def draw_star(side_length):
    for i in range(5):
        turtle.forward(side_length)
        turtle.right(144)
draw_star(100)

# Problem 4
def sum_sequence(start,stop):
    acc=0
    while start<=stop:
        acc+=start
        start+=1
    print(acc)
    return acc
sum_sequence(1,10)

# Problem 5
def division(dividend, divisor):
    acc=0
    count=0
    while acc+divisor<=dividend:
        acc+=divisor
        count+=1
    reminder=dividend-acc
    output=print(count,"R",reminder)
    return output
division(7,3)
division(4,2)

# Problem 6
def sum_digits(n):
    firstdigit=n%10
    acc=firstdigit
    while n//10!=0:
        n//=10
        onedigit=n%10
        acc+=onedigit   
    return acc
print(sum_digits(6315))

# Problem 7
import math
def geometric_mean():
    print("Please enter a non - empty sequence of positive integers, each one on aseparate line. End your sequence by typing -1: ")
    count=0
    acc=0
    endInput=False
    while not endInput:
        num=int(input())
        if num==-1:
            endInput=True
        else:
            acc+=num
            count+=1
    value=math.pow(acc,1/count)
    return value
print(geometric_mean())

# Problem 8
def fibonnaci(n):
    first=0
    second=1
    sumnum=1
    print(sumnum)
    for i in range(n-1):
        sumnum=first+sumnum
        first=second
        second=sumnum
        print(sumnum)
fibonnaci(7)
