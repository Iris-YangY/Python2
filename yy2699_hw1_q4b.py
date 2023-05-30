# Pat McYadi Yang
# CS - UY 1114
# 6 Feb 2019
# Homework 1
import math
pounds=input("Please enter weight in pounds: ")
inches=input("Please enter height in inches: ")
weight=float(pounds)*0.453592
height=float(inches)*0.0254
bmi=float(weight)/(math.pow(float(height),2))
print("BMI is: ",bmi)
