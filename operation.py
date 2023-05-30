def evaluate_expression(left_operand, right_operand, operator):
    if operator=="+":
        result=left_operand+right_operand
    elif operator=="-":
        result=left_operand-right_operand
    elif operator=="*":
        result=(left_operand)*(right_operand)
    elif operator=="/":
        result=(left_operand)/(right_operand)
    else:
        result="Error! Check your input!"
    return result
left_operand=int(input("Enter the first value: "))
right_operand=int(input("Enter the second value: "))
operator=input("Enter the operator: ")
output=evaluate_expression(left_operand, right_operand, operator)
print(output)
