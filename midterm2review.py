def less_than_10s(nums):
    total=0
    newlist=[]
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            total+=nums[i][j]
        if total<10:
            newlist.append(nums[i])
            total=0
        else:
            total=0
    return newlist
print(less_than_10s([[5,10], [1,2,3], [8,1], [9,1]]))

"""
new_lst=[]
for lst in nums:
    int_sum=0
    for num in lst:
        int_sum+=num/int_sum=sum(lst)
    if int_sum<10:
        new_lst.append(lst)
return new_lst
"""

def first_instances_only(s):
    string=""
    for item in s:
        if not item in string:
            string+=item
    return string
print(first_instances_only("Green eggs and spam"))
"""
new_str=[]
for item in s:
    if not itme in new_str:
        new_str.append(item)
return "".join(new_str)
"""

def count_chars(s):
    char=[]
    for ch in s:
        if not ch in char:
            char.append(ch)
    for i in range(len(char)):
        my_count=s.count(char[i])
        char[i]=(char[i],my_count)
    return char
print(count_chars("green"))

def most_common(s):
    info=count_chars(s)
    bignum=0
    ch=""
    for i in range(len(info)):
        if info[i][1]>bignum:
            bignum=info[i][1]
            ch=info[i][0]
    return ch
print(most_common("green"))


