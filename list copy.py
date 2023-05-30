def find_vowel_ending(lst):
    my_lst=[]
    for word in lst:
        if word[-1] in 'aeiou':
            my_lst.append(word)
    return my_lst
#print(find_vowel_ending(["hello","stop","yield","go"]))

def find_longest_word(string):
    new_str=""
    lst=string.split()
    for i in lst:
        if len(i)>len(new_str):
            new_str=i
    return new_str
#print(find_longest_word("The quick brown fox jumped over the lazy dog"))

def remove_vowels(string):
    """
    new_str=""
    for i in string:
        if not i in 'aeiou':
            new_str+=i
    return new_str
    """
    new_lst=[]
    for i in string:
        if not i in "aeiou":
            new_lst+=i
    new_string="".join(new_lst)
    return new_string
#print(remove_vowels("computer science"))

def two_dimensional_lst_sum(lst):
    lstsum=0
    for i in lst:
        for j in i:
            lstsum+=j
    return lstsum
#print(two_dimensional_lst_sum([[1,2,3],[4,5,6],[7,8]]))

