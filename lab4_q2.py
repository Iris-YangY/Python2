import random
def rand_eval():
    # sig : () -> NoneType
    num=random.randint(-100,100)
    if num%2==0:
        output=print(num," is an even number")
    else:
        output=print(num," is an odd number")
    return output
rand_eval()
