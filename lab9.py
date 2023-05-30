# Lab 9
# Problem 1
'''
The func1 function takes an list and a variable as parameters
and as a mutating function, it returns a list that each items
of the original list adds the variable 'var'.
The func2 function takes a list and a variable as parameters
and ad a mutating function, it returns a list that each items
of the original list adds 5.
The func3 function takes a list as a parameter and as a
mutating function, it returns a list that pop last items of
the originals list.
The func4 function takes a list as a parameter and as a
mutating function, it returns a list that print everything
in the original list except the last item.
The main function calls all functions from func1 to func4,
the first output would be [5,6,7], and the second is [8,9,10],
the third output is [2,3], and the fourth is[2]
'''

# Problem 2
def consecutive_numbers(filename, n):
    file_write_obj=open(filename,"w")
    for i in range(n):
        file_write_obj.writelines(str(i+1)+'\n')
    file_write_obj.close()
#consecutive_numbers("numbers.txt", 5)'

# Problem 3
def square_numbers(filename, ourFile):
    main_lst=[]
    squared_lst=[]
    file_obj=open(filename)
    for line in file_obj:
        new_lst=line.split()
        main_lst.append(new_lst)
    file_write_obj=open(ourFile,"w")
    for i in range(len(main_lst)):
        squared_lst.append(int(i+1)**2)
        file_write_obj.writelines(str(squared_lst[i])+'\n')
    file_write_obj.close()
#square_numbers("numbers.txt", "num_squared.txt")

# Problem 4
def get_data_list(file_name):
    file_obj=open(file_name,"r")
    main_lst=[]
    for line in file_obj:
        new_lst=line.strip().split(",")
        main_lst.append(new_lst)
    file_obj.close()
    return main_lst
lst = get_data_list("TSLA.csv")

def get_monthly_average(data_list):
    i=1
    total=0
    count=0
    average=0
    date=lst[i][0][:7]
    monthly_averages_list=[]
    while i <= len(data_list)-1:
        while lst[i][0][:7]==date:
            i+=1
            count+=1
            if i>len(data_list)-1:
                break
            total=float(lst[i][5])*float(lst[i][6])    
        if i>len(data_list)-1:
            break
        average=total/count
        app=(date, average)
        monthly_averages_list.append(app)
        date=lst[i][0][:7]
        count=0
    return monthly_averages_list
monthly_averages_list=(get_monthly_average(lst))

def print_info(monthly_averages_list):
    newlist=[]
    infolist=[]
    finallist=[]
    for i in range(len(monthly_averages_list)):
        new=(monthly_averages_list[i][1], monthly_averages_list[i][0])
        newlist.append(new)
    newlist.sort()
    for i in range(1,7,1):
        final=newlist[-i]
        finallist.append(final)
    for i in range(6,0,-1):
        final=newlist[i]
        finallist.append(final)
    for i in range(len(finallist)):
        new=(finallist[i][1],finallist[i][0])
        infolist.append(new)
    print(infolist)
#print_info(monthly_averages_list)    

# Problem 5
def k_shift(lst, k):
    newlist=[]
    for i in range(k,0,-1):
        new=lst[-i]
        newlist.append(new)
    for i in range(len(lst)-k):
        new=lst[i]
        newlist.append(new)
    return newlist
def k_shift_inplace(lst,k):
    for i in range(len(lst)-k):
        lst.append(lst[i])
    for j in range(len(lst)//2):
        lst.pop(0)
