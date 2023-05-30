'''file_write_obj=open("new_file.txt",'a')
file_write_obj.write("new file")
file_write_obj.close()

'''
file_obj=open("new_file.txt")
main_lst=[]
for line in file_obj:
    new_lst=line.split()
    main_lst.append(new_lst)
file_obj.close()
print(main_lst)
print(len(main_lst))

for line_lst in  main_lst:
    for word in line_lst:
        print(word)
file_obj.close()
file_obj=open("new_file.txt")
'''print(file_obj.readline())
print(file_obj.readline())
print(file_obj.readline())'''
print(file_obj.readlines())
file_obj.close()

file_write_obj=open("new_file.txt","w")
file_write_obj.writelines("write a new line")
file_write_obj.close()
