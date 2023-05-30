def leap_year(year):
    if year%100==0:
        if year%400==0:
            output="True"
        else:
            output="False"
    elif year%4==0:
        output="True"
    else:
        output="False"
    return output
year=int(input("Enter a year to check: "))
output=leap_year(year)
print(output)
