# Problem 1
"""
1.
[15, 4, 7]
2.
[1, 57, 25, 1, 57, 25, 1, 57, 25]
3.
["good", "better", "best"]
["good", "good"]
4.
[0, 1, 4]
5.
[3, 4, 4, 5, 5, 6]
"""
# Problem 2
def powers_of_two_lst(n):
    lst=[]
    for i in range(n):
        lst.append(2**(i+1))
    print(lst)

# Problem 3
def my_count(lst, val):
    count=0
    for i in range(len(lst)):
        if lst[i]==val:
            count+=1
    print(count)

# Problem 4
def get_common_elems(lst1, lst2):
    my_lst=[]
    for i in range(len(lst1)):
        for k in range(len(lst2)):
            if lst1[i]==lst2[k]:
                my_lst.append(lst1[i])
    print(my_lst)

# Problem 5
def count_digits(val):
    count_lst=[0]*10
    count=0
    while val>0:
        count_lst[val%10]+=1
        val//=10
    return count_lst
def print_digits(lst):
    for i in range(len(lst)):
        if lst[i]>0:
            print(i,"appears",lst[i],"times")
def main():
    print_digits(count_digits(3292019))
main()
