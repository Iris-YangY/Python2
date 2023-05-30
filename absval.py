def abs_val(x):
    if x>=0:
        x=x
    if x<0:
        x=-x
    return x
x=int(input("Enter the value of x: "))
value=abs_val(x)
print(value)
