# Pat McYadi Yang
# CS - UY 1114
# 6 Feb 2019
# Homework 1
print("Please enter number of coins.")
quarter=input("Number of quarters: ")
dime=input("Number of dimes: ")
nickel=input("Number of nickels: ")
penny=input("Number of pennies: ")
total=25*(int(quarter))+10*(int(dime))+5*(int(nickel))+1*(int(penny))
dollar=total//100
cent=total%100
print("The total is ",dollar," dollars and ",cent," cents.")
