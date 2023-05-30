import math
def get_digit(value, position):
    output=(value//(math.pow(10,position)))%10
    return output
value=int(input("Enter the value: "))
position=int(input("Enter the position: "))
output=get_digit(value,position)
print("The value of ", value, " in 10 of ", position, " position is ", output)
    
