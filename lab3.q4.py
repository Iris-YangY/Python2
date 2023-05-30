import math
def find_circumference(radius):
    circum=2*(math.pi)*radius
    return circum
radius=int(input("Enter the radius: "))
circum=find_circumference(radius)
print("The circumference is ", circum)

def print_circum(radius, circum):
    print("The circumference of a circle with radius ", radius, " is ", circum)

print_circum(radius, circum)
