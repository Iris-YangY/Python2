def mystery1(x):
    """signature: str -> str"""
    for z in ["yes", "no", "maybe"]:
        if x == z:
            return z
    return "unknown"
print(mystery1("Maybe"))
def mystery2(lst):
    """signature: list(str) -> str """
    acc = ""
    for item in lst:
        acc += item+", "
    return acc
print(mystery2(["abc","b","c"]))
def mystery3(lst):
    """signature: list(int) -> list(int) """
    i=0
    while i < len(lst) // 2:
        lst[i] += lst[i + len(lst) // 2]
        i+=1
    return lst[0:len(lst) // 2]
print(mystery3([2,3,5]))
def mystery4():
    """signature: () -> list(str) """
    acc = []
    for first in [1, 2, 3]:
        for second in ["a", "b", "c"]:
            acc.append(first * second)
    return acc
print(mystery4())
