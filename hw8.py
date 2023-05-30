def respell(string):
    respellings = { "teh": "the",
                    "relevent": "relevant",
                    "lite": "light",
                    "lol": "haha",}
    old = string.split()
    for i in range(len(old)):
        if old[i] in respellings:
            old[i] = respellings[old[i]]
    new_str = " ".join(old)
    return new_str
print(respell("I ate teh whole thing lol"))


def word_positions(string):
    lst = string.split()
    D = {}
    for i in range(len(lst)):
        if lst[i] not in D:
            D[lst[i]] = [i]
        else:
            D[lst[i]].append(i)
    return D
print(word_positions('It was the best of times it was the worst of times'))
            

def commonest(D):
    my_str = ""
    length=0
    for key, value in D.items():
        if len(value) > length:
            length=len(value)
            my_str = key
    return my_str
            
print(commonest(word_positions("He thought a thought he'd never thought before")))
