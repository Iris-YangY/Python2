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
firstx=float(input("What is the x-coordinate of the first point?"))
firsty=float(input("What is the y-coordinate of the first point?"))
secondx=float(input("What is the x-coordinate of the second point?"))
secondy=float(input("What is the y-coordinate of the second point?"))
distance=distance(firstx,firsty,secondx,secondy)
print("The distance between (",firstx," , ",firsty,") and (",secondx," , ",secondy,") is ",distance,".")
