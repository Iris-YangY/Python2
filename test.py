#problem 6
def intersperse():
    first = input("Enter a sentence:").split()
    second = input("Enter a sentence:").split()
    rslt = []
    if len(first) > len(second):
        for item in range(len(second)):
            rslt.append(first[item])
            rslt.append(second[item])
        rslt.append(first[len(second):])
        rslt = " ".join(rslt)
    else:
        for item in range(len(first)):
            rslt.append(first[item])
            rslt.append(second[item])
        rslt.extend(second[len(first):])
        rslt = " ".join(rslt)
    return rslt
intersperse()

#problem 7
def rlencode(s):
    count = 1
    my_lst = []
    for item in range(1,len(s)):
        if s[item-1] == s[item]:
            count += 1
        else:
            my_lst.append((s[item-1],count))
            count = 1
    my_lst.append((s[item],count))
    return my_lst

def rldecode(rle):
    string = ""
    for i in range(len(rle)):
        string += rle[i][1] * rle[i][0]
    return string
print(rlencode("1111111"))
print(rldecode(rlencode("Hello!")))
