def lower(n):
    count=0
    blank = n-1
    for count in range(n):
        numasterisks=count*2+1
        print(blank*" "+numasterisks*"*")
        numasterisks+=2
        blank-=1

