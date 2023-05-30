# Pat McYadi Yang
# CS - UY 1114
# 17 Feb 2019
# Homework
# Problem 1
def x(y):
    print(y * 2)
    return y + 1
def q(v, z):
    z = x(z)
    w = z + x(v)
    print(w)
q(30, 5)
"""
10
60
37
"""

def c():
    print("C")
def b():
    print("B1")
    c()
    print("B2")
def a():
    print("A1")
    b()
    print("A2")
a()
"""
A1
B1
C
B2
A2
"""
def second(s):
    s = s +"!"
    return s
def first(s):
    return second(s) + second(s)
print(first("Ok"))
"""
Ok!Ok!
"""
# Problem 2
def print_top (offset) :
    # signature: int -> NoneType
    print (offset * ' ' + '^')
def print_middle (offset , width) :
    # signature: int , int -> NoneType
    print (offset * ' ' + '/' + width * ' ' + '\\')
def print_bottom (offset , width):
    # signature: int , int -> NoneType
    print (offset * ' ' + width * '-')
"""offset indicates for how far of the output should be to the leftside,
and the width indicates for how far in print_middle() two signs of /\ should
be, as well as for how many in print_bottom sign - should be"""

def print_triangle():
    print_top(4)
    print_middle(3,1)
    print_middle(2,3)
    print_middle(1,5)
    print_bottom(1,7)
print_triangle()
# Problem 3
def double (n) :
    # signature: int -> int
    # return doubled value of parameter
    return n * 2
def succ (n) :
    # signature: int -> int
    # returns successor of parameter
    return n + 1
def f (n) :
    # signature: int -> int
    # returns the value 2*n + 1
    n=double(n)
    n=succ(n)
    return n
def g (n) :
    # signature: int -> int
    # returns the value 4*n
    n=double(n)
    n=double(n)
    return n
def h (n) :
    # signature: int -> int
    # returns the value 8*n + 4
    n=g(n)
    n=f(n)
    n=succ(n)
    n=succ(n)
    n=succ(n)
    return n
# Problem 4
import math
def hypotenuse(a,b):
    """
    sig: float , float -> float
    """
    h=math.sqrt(a**2+b**2)
    return h
a=25.0
b=5.0
print(hypotenuse(a,b))
# Problem 5
def distance(x1,y1,x2,y2):
    """
    signature: float , float , float , float -> float
    returns the distance between the coordinates (x1 , y1) and (x2 , y2)
    in the cartesian plane
    """
    xdistance=x2-x1
    ydistance=y2-y1
    distance=hypotenuse(xdistance,ydistance)
    return distance
x1=27
y1=6
x2=2
y2=1
output=distance(x1,y1,x2,y2)
print(output)
# Problem 6
def interactive_distance():
    firstx=float(input("What is the x-coordinate of the first point?"))
    firsty=float(input("What is the y-coordinate of the first point?"))
    secondx=float(input("What is the x-coordinate of the second point?"))
    secondy=float(input("What is the y-coordinate of the second point?"))
    distancebetween=distance(firstx,firsty,secondx,secondy)
    output=print("The distance between (",firstx," , ",firsty,") and (",secondx," , ",secondy,") is ",distancebetween,".")
    return output
interactive_distance()
