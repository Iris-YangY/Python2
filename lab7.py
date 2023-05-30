# Problem 1
'''
1(a)
x[1]
x[11]
(b)
x[len(x)-1]
(c)
x[0:4]
2(a)
my_str[0:3]
(b)
my_str[4:8]
3(a)
my_str2[0:(len(my_str2)/2)]
(b)
my_str2[(len(my_str2)/2):len(my_str2)]
4(a)
my_str3[(len(my_str3))//2]
(b)
my_str3[0:(len(my_str3)//2)]
(c)
my_str3[(len(my_str3)//2:len(my_str3)]
5(a)
Wa syu ae
(b)
y si t
'''
# Problem 2
def names_equal(name1,name2):
    count1=0
    start=0
    stop=0
    for count1 in range(len(name1)):
        if name1[count1]==",":
            stop=count1
            break
    lastname1=name1[0:stop]
    start=stop+2
    stop=len(name1)
    firstname1=name1[start:stop]
    count2=0
    for count2 in range(len(name2)):
        if name2[count2]==" ":
            break
    firstname2=name2[0:count2]
    lastname2=name2[count2+1:len(name2)]
    if lastname1==lastname2 and firstname1==firstname2:
        return True
    else:
        return False
# Problem 3
def find_Hamming_dist(str1, str2):
    count=0
    acc=len(str1)
    for count in range(len(str1)):
        if str1[count]==str2[count]:
            acc-=1
    return acc
# Problem 4
def count_succ_digits(input_val):
    count=0
    start=0
    stop=0
    print("Your string has:")
    for count in range(len(input_val)-1):
        if input_val[count]==input_val[count+1]:
            stop+=1
        else:
            print(stop-start+1,input_val[count],"\'s")
            start=stop
    lastword=print(stop-start+1, input_val[count+1], "\'s")
# Problem 5
def is_palindrome(input_str):
    count=0
    new_count=0
    for count in range(len(input_str)):
        new_count=(count+1)*-1
        if input_str[count]==input_str[new_count]:
            return True
        else:
            return False
# Problem 6
def hide_num_info(input_str):
    start=-1
    stop=0
    pin=""
    acc=""
    for i in range(len(input_str)):
        if input_str[i]==" ":
            stop=i
            pin=input_str[start+1:stop+1]
            if pin.isdigit():
                acc+=len(pin)*"x"
            else:
                acc+=pin
            start=stop
    stop=len(input_str)
    lastword=input_str[start+1:stop]
    acc+=lastword
    return acc
print(hide_num_info("My userID is john17 and my 4 digit pin is 1234 which is secret"))
