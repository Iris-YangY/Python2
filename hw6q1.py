def mystery1(x):
    """
    for z in ["yes", "no", "maybe"]:
        if x == z:
            return z
    return "unknown"
print(mystery1("Maybe"))
def mystery2(lst):
    """
    acc = ""
    for item in lst:
        acc += item+", "
    return acc
print(mystery2(["abc","b","c"]))
def mystery3(lst):
    """
    i=0
    while i < len(lst) // 2:
        lst[i] += lst[i + len(lst) // 2]
        i+=1
    return lst[0:len(lst) // 2]
print(mystery3([2,3,5]))
def mystery4():
    """
    acc = []
    for first in [1, 2, 3]:
        for second in ["a", "b", "c"]:
            acc.append(first * second)
    return acc
print(mystery4())