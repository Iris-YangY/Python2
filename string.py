def count_char(string, char):
    count=0
    for ch in string:
        if ch==char:
            count+=1
    return count

def replace_char(string, char):
    new_str=""
    for ch in string:
        if ch==char:
            new_str+="*"
        else:
            new_str+=ch
    return new_str
#print(replace_char("hello","e"))
#len(my_str)-starts at 1
def reverse_string(string):
    new_str=""
    for i in range(len(string)-1,-1,-1):
        ch=string[i]
        new_str+=ch
    return new_str
#print(reverse_string("hello"))
my_str = "hello world"
#my_str.name_of_method()
#print(my_str.capitalize())
#print(my_str.upper())
print(my_str.find('lo'))
