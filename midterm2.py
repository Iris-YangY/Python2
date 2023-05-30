def main():
    in_file=open("in.csv", "r")
    total=0
    count=0
    for line in in_file:
        lst=line.strip().split(',')
        for ind in range(len(lst)):
            lst[ind]=float(lst[ind])
        val=sum(lst[:-1])
        result=val*lst[-1]
        total+=result
        print(count,result)
        count+=1
    print(total)
    in_file.close()
#main()

def find_room(rooms, students):
    main_lst=[]
    for j in range(len(students)):
        if j>=rooms[0][0] and j<=rooms[0][1]:
            new_lst1+=students[j]
        elif j>=rooms[1][0] and j<=rooms[1][1]:
            new_lst2+=students[j]
        else:
            new_lst2.append([])
    main_lst.append(new_lst1)
    main_lst.append(new_lst2)
    return main_lst

def get_data(filename):
    file_obj=open(filename)
    main_lst=[]
    for line in file_obj:
        lst=line.strip.splie(",")
        for i in range(len(lst)):
            new_lst+=(float(lst[i]))
    file_obj.close()
    main_lst.append(new_lst)
    return main_lst

"""def htl(hashtag):
    word=""
    main_lst=[]
    i=1
    while i<(len(hashtag)):
        if i+1>len(hashtag):
            break
        if hashtag[i].isupper()==True:
            word+=hashtag[i]
        elif hashtag[i-1].islower()==True and hashtag[i].isupper()==True:
            main_lst.append(word.lower())
            word=""+hashtag[i]
        elif hashtag[i].islower()==True:
            word+=hashtag[i]
        print(word)
        i+=1
    return main_lst
"""


def htl(hashtag):
    i=1
    numlist=[]
    mainlst=[]
    for i in range(len(hashtag)):
        if hashtag[i].isupper()==True:
            numlist.append(i)
    print(numlist)
    start=1
    for j in range(len(numlist)):
        if numlist[j]=start:
            end=int(numlist[j+1])
            word=hashtag[start:end]
        print(word)
        start=int(j)+1
        mainlst.append(word.lower())
    return mainlst
print(htl('#SpatulaKing'))
        
