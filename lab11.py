# Pat McYadi Yang
# CS - UY 1114
# 19 Apr 2019
# Lab 11

# Problem 1
'''
a. 82
b. 'Jennifer'
c. {"Jennifer":13 , "Asher":30 , "Jeff":19 , "Chitra":23}
'''

# Problem 2
# a.
my_dict = {"a": 15 , "c": 35 , "b": 20}
for key in my_dict:
    print(key)
# b.
for value in my_dict.values():
    print(value)
# c.
for key, value in my_dict.items():
    print(key, value)
# d.
lst=[]
for key, value in my_dict.items():
    dicttuple=(key, value)
    lst.append(dicttuple)
    lst.sort()
print(lst)
# e.
lst=[]
for key, value in my_dict.items():
    dicttuple=(value, key)
    lst.append(dicttuple)
    lst.sort()
newlst=[]
for item in lst:
    newtuple=(item[1], item[0])
    newlst.append(newtuple)
print(newlst)

# Problem 3
def count_digits(lst):
    my_dict={}
    for string in lst:
        if string in my_dict:
            my_dict[string]+=1
        else:
            my_dict[string]=1
    return my_dict
print(count_digits([1,2,3]))
print(count_digits([2,0,1,9,0,4,1,9]))
