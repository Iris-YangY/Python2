# Problem 1
# 13
def func1 ( x ):
    if 10 > x >= 5:
        x -= 4
    if 10 > x >= 5:
        return x
    else :
        return x + 10
print(func1(7))

# 3
def func2 ( x ):
    if 10 > x >= 5:
        x -= 4
        return x
    elif 10 > x >= 5:
        return x
    else :
        return x + 10
print(func2(7))

# 16
def func3 ( y ):
    if y > 7:
        y += 1
    elif y > 10:
        y += 1
    elif y > 15:
        y += 1
    return y
print(func3(15))

# 18
def func4 ( y ):
    if y > 7:
        y += 1
    if y > 10:
        y += 1
    if y > 15:
        y += 1
    return y
print(func4(15))

# 144
def func5 ( y ):
    x = 0
    if y % 2 == 0:
        if y > 5:
            x = y ** 2
        else :
            x += 1
    else :
        if y > 5:
            y = y ** 2
        else :
            y += 1
    return x
print(func5(12))
