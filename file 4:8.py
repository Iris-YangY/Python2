def read_data(filename):
    main_list=[]
    file_obj=open(filename,"r")
    for line in file_obj:
        new_list=line.strip().split(",")
        main_list.append(new_list)
    file_obj.close()
    main_list.pop(0)
    return main_list
main_list=read_data("Yankees_roster.csv")


def write_data(lst):
    namelist=[]
    for i in lst:
        if i[4]=="Pitcher":
            namelist.append(i[2]+"\n")
    namelist.sort()
    file_obj=open("pitchers.txt","w")
    file_obj.writelines(namelist)
    file_obj.close()
name_list=write_data(main_list)
        
def convert_to_int(string):
    try:
        if string.isdigit():
            num=int(string)
            return num
        else:
            raise ValueError(string)
    except ValueError:
        print("Can not convert \"", string, "\" to int")

def read_data2(filename):
    main_list=[]
    file_obj=open(filename)
    for line in file_obj:
        new_list=line.strip().split(",")
        main_list.append(new_list)
    file_obj.close()
    main_list.pop(0)
    return main_list
main_list2=read_data2("TTred_raiders.csv")

def find_avg_height(roster):
    heightlist=[]
    feet=0
    inches=0
    for i in roster:
        height=i[4].split("'")
        heightlist.append(height)
    for j in heightlist:
        feet+=int(j[0])*12
        inches+=int(j[1])
    num=len(heightlist)
    avg=(feet+inches)/(12*num)
    return avg
avg=find_avg_height(main_list2)
