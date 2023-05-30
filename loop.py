"""def count_up(n):
    count=1
    while count<=n:
        print(count)
        count+=1
count_up(3)"""

def even_sum(n):
    count=2
    acc=0
    while count<=n:
        acc+=count
        count+=2
    return acc
#print(even_sum(3))

def make_square(n):
    count=0
    while count<n:
        print("#"*n)
        count+=1
#make_square(4)

def factorial(n):
    count=1
    acc=1
    while count<=n:
        acc=count*acc
        count+=1
    """
    acc=1
    while n>0:
        acc*=n
        n-=1
    """
    return acc
#print(factorial(5))

import random
def find_even_randoms():
    count=0
    while count<5:
        rand_val=random.randint(0,100)
        if rand_val%2==0:
            print(rand_val)
            count+=1
#find_even_randoms()

def print_digits(n):
    while n>0:
        firstdigit=n%10
        print(firstdigit)
        n//=10
print_digits(123456789)
