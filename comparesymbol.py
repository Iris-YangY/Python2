def find_compare_symbol(x,y):
    if x>y:
        symbol=">"
    if x==y:
        symbol="=="
    if x<y:
        symbol="<"
    return symbol
x=int(input("Enter the first value: "))
y=int(input("Enter the second value: "))
compare=find_compare_symbol(x,y)
print(x, compare, y)
