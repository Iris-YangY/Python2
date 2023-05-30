def largest_odd(x):
    if x%2!=0:
        x=x
    if x%2==0:
        x=x-1
    return x
x=int(input("Enter a number to find the largest odd: "))
value=largest_odd(x)
print(value)
