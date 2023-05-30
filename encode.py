def encode(string):
    if string == '':
        return ''
    i = 0
    count = 0
    letter = string[i]
    rle = []
    lst=[]
    while i <= len(string) - 1:        
        while string[i] == letter:
            i+= 1
            count +=1
            if i > len(string) - 1:
                break
        if count == 1:
            lst=[letter, count]
            rle.append(lst)
        else:
            lst=[letter, count]
            rle.append(lst)
        if i > len(string) - 1: 
            break
        letter = string[i]
        count = 0

    return rle
print(encode("abbcc"))
