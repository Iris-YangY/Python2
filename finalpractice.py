#1. 37 int
#2. False bool
#3. 'a' string
#4. Error Error
#5. True bool
#6. Error Error
#7. ['a', 'd', 'f', 'h'] list
#8. Error Error
#9. [33, 45, 37, 26] list
#10. False bool

"Second Avenue: Color: red Cars: 4"
"First Avenue: Color: yellow Cars: 0"
"Second Avenue: Color: green Cars: 10"

-1
2
1
-1
2
1
-1
2
1

def word_count(text):
    worddict={}
    for line in text:
        newlst=line.strip().split("',.!?-")
        for i in range(len(newlst)):
            newlst[i]=newlst[i].lower()
            if newlst[i] in worddict:
                worddict[newlst[i]]+=1
            else:
                worddict[newlst[i]]=1
    return worddict

class Money:
    def __init__(self, dollars=0, cents=0):
        self.dollars=dollars
        self.cents=cents
        if self.cents>=100:
            self.dollars=dollars+self.cents//100
            self.cents=cents-self.cents//100*100
    def __str__(self):
        if self.cents>=10:
            return "$"+str(self.dollars)+"."+str(self.cents)
        else:
            return "$"+str(self.dollars)+".0"+str(self.cents)
    def __add__(self, other):
        self.dollars+=other.dollars
        self.cents+=other.cents
        return self
    def __lt__(self, other):
        return self.dollars!=other.dollars and self.cents!=other.cents
    
def main ():
    money1 = Money (1 ,102)
    money2 = Money (2 ,20)
    print (money1)
    print (money2)
    print (money1 + money2)
    print (money1 < money2)
#main()

def create_dictinary(filename):
    file_obj=open(filename,'r')
    infodict={}
    file_obj.readline()
    for line in file_obj:
        newlst=line.strip().split(",")
        infodict[newlst[0]]=(str(newlst[1]), int(newlst[2], str(newlst[3])))
    file_obj.close()
    return infodict

def find_studnets(student_dict):
    namelst=[]
    for key, value in student_dict:
        namelst.append(value[0])
    return namelst

class FuelTank:
    def __init__(self, capacity=10):
        self.capacity=capacity
        self.gallons_in=0.0
    def __str__(self):
        return str(self.gallons_in)
    def fill(self, gallons_in):
        if self.gallons_in+gallons_in>=self.capacity:
            self.gallons_in=self.capacity
        else:
            self.gallons_in+=gallons_in
    def is_empty(self):
        return self.gallons_in==0
    def get_percent_full(self):
        return self.gallons_in/self.capacity*100
    def use_fuel(self, rate_per_hour, hours):
        self.gallons_in-=rate_per_hour*hours
        if self.gallons_in<0:
            raise ValueError("ValueError! Not enough fuels!")
            self.gallons_in=0
def main ():
    tank1 = FuelTank (10)
    print ( tank1 . is_empty ()) # True
    tank1 . fill (7)
    print ( tank1 . get_percent_full ()) #70.0
    tank1 . fill (12)
    print ( tank1 . get_percent_full ()) #100.0
    tank1 . use_fuel (0.5 , 21) # ValueError Not Enough Fuel !
main ()
