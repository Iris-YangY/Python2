"""my_str='hello world'
#print(my_str[-1])
#print(my_str[4:])
#print(my_str[:5])
str1="NYU Tandon"
#print(str1[4])
#print(str1[-2])
#print(str1[0:-7])
#print(str1[-7:-4])
#print(str1[:3])
#print(str1[:])
#print(str1[1:6:2])
#print(str1[9:3:-2])
#print(str1[::2])
#print(str1[-1:3:-1])
#print(len(str1))
my_str="hello"
for i in range(len(my_str)):
    print(i)
    print(my_str[i])
string=""
print(len(string))
"""
def letter_dup(string,n):
    new=""
    for ch in string:
        new+=ch*n
    return new
#print(letter_dup("hello",3))

def remove_vowels(string):
    new=""
    for ch in string:
        """if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":"""
        if ch.lower() in 'aeiouAEIOU':
            new=new
        else:
            new+=ch
    return new
#print(remove_vowels("NYU Tandon School of Engineering"))

def make_alt_case(string):
    new=""
    for i in range(len(string)):
        if i%2==0:
            new+=string[i].upper()
        else:
            new+=string[i].lower()
    return new
#print(make_alt_case("TANDON"))

def my_find(string,char):
    for i in range(len(string)):
        if string[i]==char:
            return i
    return -1
#print(my_find('hello','l'))

def get_words(string):
    space=-1
    for i in range(len(string)):
        if string[i]==' ':
            word=string[space+1:i]
            print(word)
            space=i
    last_word = string[space+1]
    print(last_word)
get_words("a b c d e f g")
