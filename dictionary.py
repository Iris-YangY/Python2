def count_chars(s):
    char_dict={}
    for char in s:
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict[char]=1
    return char_dict
print(count_chars("green"))

def most_common(s):
    char_dict=count_chars(s)
    #mostcommon=max(char_dict)
    max_val=0
    max_ch=''
    for ch, count in char_dict.items():
        if count>max_val:
            max_val=count
            max_ch=ch
    return max_ch
print(most_common("green"))

def create_capitals_dict(filename):
    file_obj=open(filename, 'r')
    capitals={}
    for line in file_obj:
        state, city=line.strip().split(", ")
        capitals[state]=city
    return capitals
capitals=create_capitals_dict("state_capitals.csv")

'''for key, val in capitals.items():
    print(key+", "+val)'''

def main():
    caps_dict=create_capitals_dict("state_capitals.csv")
    print("Enter a state to return it's capital city. Enter -1 to stop: ")
    endInput=False
    while not endInput:
        input_state=input()
        if input_state=="-1":
            endInput=True
        else:
            try:
                print(caps_dict[input_state])
            except KeyError:
                print("Not a valid state.")
