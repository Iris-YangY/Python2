def title_case(string):
    acc=""
    count=0
    while count<(len(string)):
        if count==0:
            acc+=string[count].upper()
        elif string[count-1] in '\'.,;:?! ' and string[count].isalpha:
            acc+=string[count].upper()
        else:
            acc+=string[count]
        count+=1
    return acc
print(title_case('3d t.v.'))
