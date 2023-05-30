# Pat McYadi Yang
# CS - UY 1114
# 31 Mar 2019
# Homework 6

# Problem 1
def read_file(filename):
    file_obj=open(filename,"r")
    main_list=[]
    for line in file_obj:
        new_lst=line.strip().split(",")
        main_list.append(new_lst)
    file_obj.close()
    main_list.pop(0)
    return main_list
colleges=read_file("colleges.csv")

# Problem 2
def find_most_exclusive_womens_college(colleges):
    i=0
    admrate=1.0
    collegename=colleges[i][3]
    while i < (len(colleges)):
        if colleges[i][24]!="NULL":
            if int(colleges[i][22])==1 and float(colleges[i][24])<float(admrate):
                collegename=colleges[i][3]
                i+=1
            else:
                i+=1
        else:
            i+=1
    return collegename
collegename=find_most_exclusive_womens_college(colleges)

# Problem 3
def average_sat_score_in_ny(colleges):
    i=0
    totalscore=0
    totalnum=0
    while i < len((colleges)):
        if colleges[i][5]=="NY" and colleges[i][25]!="NULL":
            totalnum+=1
            totalscore+=float(colleges[i][25])
            i+=1
        else:
            i+=1
    average=totalscore/totalnum
    return average
average=average_sat_score_in_ny(colleges)

# Problem 4
def distance(first, second):
    distance=((first[0]-second[0])**2+(first[1]-second[1])**2)**0.5
    return distance
distance((40.730610, -73.935242), (34.052235, -118.243683))

# Problem 5
def find_college_nearest_center_of_us(colleges):
    first=(39.833333, -98.583333)
    i=0
    second=(float(colleges[i][18]),float(colleges[i][19]))
    result=distance(first,second)
    name=colleges[i][3]
    for i in range(len(colleges)):
        if colleges[i][18]!="NULL" and colleges[i][19]!="NULL":
            second=(float(colleges[i][18]),float(colleges[i][19]))
            if distance(first,second)<result:
                result=distance(first,second)
                name=colleges[i][3]
    return name
name=find_college_nearest_center_of_us(colleges)

# Problem 6
def main():
    colleges=read_file("colleges.csv")
    collegename=find_most_exclusive_womens_college(colleges)
    average=average_sat_score_in_ny(colleges)
    name=find_college_nearest_center_of_us(colleges)
    print("Most exclusive women's college: ",collegename)
    print("Average SAT of all NY schools: ",average)
    print("College nearest geographical center of contiguous US: ",name)

