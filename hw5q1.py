def mystery1(s):
# sig: str -> str
    i=0
    acc = ""
    while i < len(s):
        acc += s[i]
        i+=2
    return acc
print(mystery1("hello"))
def mystery2(s, i):
# sig: str, int -> str
    acc = ""
    while i < len(s):
        acc += s[i] + s[(i + 1) * -1]
        i+=1
    return acc
print(mystery2("abcd",1))
def mystery3(s, v):
# sig: str, str -> int
    acc = 0
    for ch in s:
        if ch in v:
            acc += 1
    return acc
print(mystery3("abcdefg","apple"))
def mystery4(s):
# sig: str -> str
    i=1
    acc = ""
    while i < len(s):
        if s[i - 1].isdigit():
            acc += s[i]
        i+=1
    return acc
print(mystery4("1a2b3c4d56e"))
