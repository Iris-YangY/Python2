# Pat McYadi Yang
# CS - UY 1114
# 15 Mar 2019
# Homework 5

# Problem 1
'''
for mystery1, the program takes a string as a
parameter and then returns a string containing
the first, thrid, fifth...until the last character
of the original string.
mystery1("hello")=="hlo"
for mystery2, the program takes a string and an
integer as parameters and then returns a string
containing from the i character and the last i
character of the original string, to the character
after i and the charater before the last i
characterof the original string, to the last
character and the first character of the string.
mystery2("abcd" ,1)=="bccbda"
for mystery3, the program takes two strings as
parameters and then returns an integer of how many
of a specific character, as indicated in the program
of parameter s, appears in the original string v.
mystery3("abcdefg","apple")==2
for mystery4, the program takes a string as a
parameter and then returns a string containing
characters starting from the second position of
the original string, returns a new string containing
character after each number in the original string
orderrly.
mystery4("1a2b3c4d56e")==abcd6e
'''
# Problem 2
def replace_spaces(string):
    acc=""
    for ch in string:
        if ch==" ":
            acc+="_"
        else:
            acc+=ch
    return acc
# Problem 3
def has_punctuation(string):
    for ch in string:
        if ch in '\'.,;:?!':
            return True
    return False
# Problem 4
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
# Problem 5
def is_valid_password(string):
    uppercount=0
    lowercount=0
    digitcount=0
    charactercount=0
    if len(string)>=8:
        for ch in string:
            if ch.isupper():
                uppercount+=1
            elif ch.islower():
                lowercount+=1
            elif ch.isdigit():
                digitcount+=1
            elif ch in "!@#$":
                charactercount+=1
        if uppercount>=2 and lowercount>=1 and digitcount>=2 and charactercount>=1:
            return True
        else:
            return False
    else:
        return False
# Problem 6
def calc(string):
    start=0
    stop=0
    operand1=0
    operand2=0
    result=0
    for i in range(len(string)):
        if string[i]==" ":
            stop=i
            break
    operand1=int(string[start:stop])
    start=i+3
    operand2=int(string[start:len(string)])
    operator=string[i+1]
    if operator=="+":
        result=operand1+operand2
    elif operator=="-":
        result=operand1-operand2
    elif operator=="*":
        result=operand1*operand2
    return result
# Problem 7
def finder(needle,haystack):
    length=len(needle)
    for i in range(len(haystack)-length+1):
        if haystack[i:length+i]==needle:
            return i
    else:
        return -1  
