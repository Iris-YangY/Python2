def approx_div(x,y):
    if y!=0:
        x=x/y
    else:
        x=x/0.0000001
    return x
x=int(input("Enter the first value: "))
y=int(input("Enter the second value: "))
value=approx_div(x,y)
print(value)
