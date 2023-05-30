"""price=float(input("Enter the price of the meal: "))
add_tip=price*1.2
print("The total for a meal costing $ ", price, "including a 20% tip is $ ", add_tip)"""

"""def tip_calculator(meal_cost, tip):
    total = meal_cost+meal_cost*tip/100
    return total

def tip_calculator_15(meal_cost):
    total = meal_cost*1.15
    return total_15

tip3=18

meal_cost=float(input("Enter the price of the meal: "))
total_20=tip_calculator(meal_cost,20)
total_15=tip_calculator(meal_cost,15)
total_18=tip_calculator(meal_cost,tip3)

print_string="The total for a meal costing $ "+str(meal_cost)+" including a 20% tip is $ " + str(total_20)

print(print_string)

print("The total for a meal costing $ "+str(meal_cost)+" including a 15% tip is $ " + str(total_15))

print("The total for a meal costing $ "+str(meal_cost)+" including a ",str(tip3),"% tip is $ " + str(total_18))"""


def tip_calculator(meal_cost, tip):
    total = meal_cost+meal_cost*tip/100
    return total

def print_price(meal_cost, tip, total):
    print("The total for a meal costing $"+
    str(meal_cost)+" including a "+str(tip)+
    "% tip is $"+str(total))
    """return None"""

meal_cost=float(input("Enter the price of the meal: "))
tip1=20
tip2=18
tip3=15

total_20=tip_calculator(meal_cost,tip1)
total_18=tip_calculator(meal_cost,tip2)
total_15=tip_calculator(meal_cost,tip3)

print_price(meal_cost, tip1, total_20)
print_price(meal_cost, tip2, total_18)
print_price(meal_cost, tip3, total_15)

