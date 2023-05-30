# Pat McYadi Yang
# CS - UY 1114
# 31 Mar 2019
# Homework 6

# Problem 1
"""
Mystery1 function takes a string as a parameter
and returns a string, that is, if the string is
one of 'yes', 'no', or 'maybe', the function
returns what the parameter is, and if not, the
function returns 'unknown'
mystery1("yes")=="yes"
mystery1("what?")=="unknwon"
Mystery2 function takes a list of string as a
parameter and returns a string containing each
items in list and a comma with a space to
seperate each items
mystery2(["abc","b","c"])=="abc, b, c"
Mystery3 function takes a list of integer as a
parameter and returns a list of integer as a
result. The return is a list of integer that as
the addition from the first item and the middle
item to the one before the middle item to the
last item.
mystery3([1,2,3,4,5,6])==[5, 7, 9]
mystery3([2,3,5])==[5]
Mystery4 function takes no parameter and returns
a list of strings that contains letter 'a', 'b',
'c' for one, two, and three times.
mystery4()==['a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc']
"""

# Problem 2
def avg(numbers):
    """
    signature: list (float) -> float
    precondition: numbers != []
    returns the average (mean) of a non-empty list of floats
    """
    sumnum=0
    average=0
    for i in range(len(numbers)):
        sumnum+=numbers[i]
    average=sumnum/(len(numbers))
    return average

# Problem 3
def sum_some(lower, upper, numbers):
    total=0
    for item in numbers:
        if item>=lower:
            if item<=upper:
                total+=item
    return total

# Problem 4
def is_sorted(lst):
    sort=0
    i=1
    while i<len(lst): 
        if(lst[i]<lst[i - 1]): 
            sort=1
        i+=1
    if (not sort): 
        return True 
    else: 
        return False

# Problem 5
def indices(needle, haystack):
    my_lst=[]
    for i in range(len(haystack)):
        if haystack[i]==needle:
            my_lst.append(i)
    return my_lst

# Problem 6
def intersperse():
    import string
    my_str=""
    sentence1=input("Enter a sentence: ")
    sentence2=input("Enter a sentence: ")
    lst1=sentence1.split()
    lst2=sentence2.split()
    length=0
    if len(lst1)<len(lst2):
        length=len(lst1)
        for i in range(length):
            my_str+=lst1[i]+" "+lst2[i]+" "
        for j in range(length,len(lst2),1):
            my_str+=lst2[j]+" "
    else:
        length=len(lst2)
        for i in range(length):
            my_str+=lst1[i]+" "+lst2[i]+" "
        for j in range(length,len(lst1),1):
            my_str+=lst1[j]+" "
    print(my_str)

# Problem 7
def rlencode(s):
    my_lst=[]
    lst=[]
    count=0
    i=0
    letter=s[i]
    while i<=len(s)-1:
        while s[i]==letter:
            i+=1
            count+=1
            if i>len(s)-1:
                break
        lst=(letter, count)
        my_lst.append(lst)
        if i>len(s)-1:
            break
        letter=s[i]
        count=0
    return my_lst
def rldecode(rle):
    string=""
    for i in range(len(rle)):
        string+=rle[i][1]*rle[i][0]
    return string

# Problem 8
def reverse_pure(xs):
    my_lst=[]
    for i in range(len(xs)):
        my_lst.append(xs[-(i+1)])
    return my_lst
def reverse_mut(xs):
    for i in range(len(xs)-1, -1, -1):
        xs.append(xs[i])
    for j in range(len(xs)//2):
        xs.pop(0)
