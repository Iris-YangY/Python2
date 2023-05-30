'''def title_case(string):
    acc=""
    count=0
    while count<(len(string)):
        if count==0:
            acc+=string[count]
	elif string[count-1] in '\'.,;:?! ':
	    if string[count].isdigit():
		acc+=string[count].upper()
	    else:
		acc+=string[count]
	else:
	    acc+=string[count]
	count+=1
	print(count)
	print(acc)
    return acc
'''
def title_case(string):
    acc=""
    count=0
    while count<(len(string)):
        if count==0:
            acc+=string[count]
	elif string[count-1] in '\'.,;:?! ':
            if string[count].isdigit():
                acc+=string[count].upper()
            else:
                acc+=string[count]
        else:
            acc+=string[count]
        count+=1
        print(count)
        print(acc)
    return acc
title_case('hi')
