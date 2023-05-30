def increment_ten(x):
    return x+10
def increment_five(x):
    return x+5
def increment_two(x):
    return x+2
def increment_one(x):
    return x+1

def make_twenty_six():
    num=0
    num=increment_ten(num)
    num=increment_ten(num)
    num=increment_five(num)
    num=increment_one(num)
    return num
print(make_twenty_six())

def make_thirty_eight():
    num=0
    num=increment_ten(num)
    num=increment_ten(num)
    num=increment_ten(num)
    num=increment_five(num)
    num=increment_two(num)
    num=increment_one(num)
    return num
print(make_thirty_eight())

def make_one_thousand():
    num=0
    num=increment_ten(num)
    num=num*num*num
    return num
print(make_one_thousand())
