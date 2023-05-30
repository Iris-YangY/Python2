def celsius_to_fahrenheit(celsius_deg):
    fahrenheit=celsius_deg*1.8+32
    return fahrenheit
celsius_deg=float(input("Enter the celsius degree: "))
fahrenheit=celsius_to_fahrenheit(celsius_deg)
print(fahrenheit)

def print_conversion(c,f):
    print(c, " degrees Celsius is ", f, " degrees Fahrenheit")


def main ():
    cel_freeze = 0.0
    cel_boil = 100.0
    print_conversion ( cel_freeze , celsius_to_fahrenheit ( cel_freeze ))
    print_conversion ( cel_boil , celsius_to_fahrenheit ( cel_boil ))
main ()
