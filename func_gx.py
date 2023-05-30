def func_g(x):
    if x>=0:
        x=2*x
    if x<0:
        x=x/2
    return x
x=int(input("Enter x: "))
value=func_g(x)
print(value)
