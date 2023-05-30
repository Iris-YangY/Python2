def some_factors_string(n):
    output=""
    if n%2==0:
        output+=" 2 "
    if n%3==0:
        output+=" 3 "
    if n%4==0:
        output+=" 4 "
    if n%8==0:
        output+=" 8 "
    return output
number=int(input("Enter the value: "))
output=some_factors_string(number)
print("So the factors are: ", output)
