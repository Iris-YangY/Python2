# Pat McYadi Yang
# CS - UY 1114
# 18 Apr 2019
# Homework 8

# Problem 1
respellings={'teh':'the','relevent':'relevant','lite':'light','lol':'haha'}
def respell(string):
    newlst=[]
    slst=string.split()
    for word in slst:
        if word in respellings:
            newlst.append(respellings[word])
        else:
            newlst.append(word)
    newstring=" ".join(newlst)
    return newstring

# Problem 2
def word_positions(string):
    word_dict={}
    wordlst=string.split()
    for position in range(len(wordlst)):
        word=wordlst[position]
        if word in word_dict:
            word_dict[word].append(position)
        else:
            plst=[position]
            word_dict[word]=plst
    return word_dict

# Problem 3
def commonest(word_dict):
    new_str=''
    longest=0
    for word in word_dict:
        length=len(word_dict[word])
        if length>longest:
            longest=length
            new_str=word
    return new_str
