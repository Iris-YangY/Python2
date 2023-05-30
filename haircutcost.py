def cost_define(gender, age):
    if gender=="M" and age<=13:
            cost=15
    elif gender=="M" and age>13:
            cost=20
    if gender=="F" and age<=13:
            cost=20
    elif gender=="F" and age>13:
            cost=40
    return cost
name=input("What is your name?")
gender=input("Enter your gender: ")
age=int(input("Enter your age: "))
cost=cost_define(gender, age)
print("Hi! ",name,"! The cost for your haircut should be $",cost,"!")
