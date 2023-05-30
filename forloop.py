
def sum_input():
    print("Enter numbers to sum their value. When you are finished, enter 'X': ")
    acc=0
    endInput=False
    while not endInput:
        num=input()
        if num=="X":
            endInput=True
        else:
            acc+=int(num)
    print(acc)
    return acc
sum_input()
      
def count_up(n):
    start=1
    acc=0
    for start in range(n+1):
        acc+=start
        start+=1
    return acc
print(count_up())

def even_sum(n):
    start=2
    acc=0
    for start in range(2,n+1,2):
        acc+=start
    return acc
print(even_sum(5))

def count_down(n):
    for i in range(n,0,-1):
        print(i)
count_down(5)

def make_square(n):
    for i in range(n):
        print(" # "*n)
make_square(4)

def make_triangle(n):
    for i in range(n+1):
        print(" # "*i)
        i+=1
make_triangle(4)

def is_prime(n):
    statement=bool()
    if n>1:
        for i in range(2,n,1):
            if n%i==0:
                statement=False
            else:
                statement=True
    else:
        statement=False
    return statement

def print_primes(num):
    if num>1:
        for num in range(2,num+1,1):
            if num>1:
                for i in range(2,num):
                    if num%1==0:
                        break
                else:
                    print(num)
print_primes(12)
print_primes(12)
