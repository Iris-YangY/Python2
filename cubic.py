import math
def cubic(value):
    cubic_value=int(math.pow(value,3))
    return cubic_value
value=int(input("Enter a value, n: "))
cubic_value=cubic(value)
print("The value of ", value, " cubed is ", cubic_value)
