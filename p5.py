user=int(input("What is your number: "))
number=user
count=0
while user!=0:
    if number%10==1:
        count+=1
        number//10
    else:
        number//10
    print("1 appears ",count," time(s).")
    number=user
    if number%10==2:
        count+=1
        number//10
    else:
        number//10
    print("2 appears ",count," time(s).")
    number=user
    if number%10==3:
        count+=1
        number//10
    else:
        number//10
    print("3 appears ",count," time(s).")
    number=user
    if number%10==4:
        count+=1
        number//10
    else:
        number//10
    print("4 appears ",count," time(s).")
    number=user
    if number%10==5:
        count+=1
        number//10
    else:
        number//10
    print("5 appears ",count," time(s).")
    number=user
    if number%10==6:
        count+=1
        number//10
    else:
        number//10
    print("6 appears ",count," time(s).")
    number=user
