def mystery ( val ):
    ret_str = ""
    if val > 100:
        ret_str += " A "
    elif val > 50:
        if val % 5 == 0 and not ( val % 10 == 0):
            ret_str += " B "
        elif val % 5 == 0:
            ret_str += " C "
        else :
            ret_str += " D "
    if val > 20:
        ret_str += " E "
    else :
        ret_str += " F "
    return ret_str
#print ( mystery (75))
#print ( mystery (105))
#print ( mystery (32))
#print ( mystery (15))


def mystery ():
    x = "1"
    for i in range (1 , 5):
        if i % 3 == 0:
            x = "2"
        elif i % 2 == 0:
            x = "3"
        print ( x * i )
#mystery ()

def top_func ( val ):
    if val > 10:
        return val // 10
    else :
        return val - 1
def bottom_func ( val ):
    val = top_func ( val )
    val = top_func ( val )
    return val
result = bottom_func (35)
#print ( result )

def is_pay_legal(hr_wage, tipped):
    if tipped=="Y":
        if hr_wage>=8.65:
            return True
        else:
            return False
    elif tipped=="N":
        if hr_wage>=13:
            return True
        else:
            return False
#print(is_pay_legal(13.00, "N"))
#print(is_pay_legal(9.00, "Y"))
#print(is_pay_legal(20.00, "N"))
#print(is_pay_legal(5.00, "N"))

def calc_lab_average():
    print("Enter lab grades for the student . When finished , enter -1:")
    count=0
    acc=0
    endinput=False
    while not endinput:
        grade=input()
        if grade=="-1":
            endinput=True
        else:
            acc+=int(grade)
            count+=1
    final=acc/count
    print(final)
calc_lab_average()
