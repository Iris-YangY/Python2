class ClassName():
    
    #self.class_attribute="my_data"

    def __init__ (self, class_attr="my_data"):
        self.class_attribute=class_attr

    def __str__ (self):
        return self.class_attribute

    def __repr__(self):
        return str(self)
        #return self.class_attribute
    
    def get_attribute(self):
        return self.class_attribute
    
    def update_attribute(self, data):
        self.class_attribute=data

obj1=ClassName()
obj2=ClassName("other_data")
#obj1.class_method()
#print(obj1)
#print(obj2)
#print(obj1.get_attribute())
#print(obj2.get_attribute())
#print(obj1.class_attribute)
#obj1.class_attribute=35.7 or "new_data"
#obj1.update_attribute("new_data")
#print(obj1.get_attribute())

class Point():
    def __init__(self, x=0.0, y=0.0):
        self.x=x
        self.y=y
    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"
    def distance(self, other):
        return ((self.x-other.x)**2+
        (self.y-other.y)**2)**0.5
    def sum(self, other):
        new_point_x= (self.x+other.x)
        new_point_y=(self.y+other.y)
        return Point(new_point_x, new_point_y)
    def __add__(self, other):
        new_x=self.x+other.x
        new_y=self.y+other.y
        return Point(new_x, new_y)
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    def __mul__(self, other):
        new_x=self.x*other
        new_y=self.y*other
        return Point(new_x, new_y)
    def __rmul__(self, other):
        return self*other
p1=Point(1.0,1.0)
p2=Point(2.0,3.0)
print(p1)
#print(p2)
res=p1.distance(p2)
p3=p1.sum(p2)
p4=p1+p2
#print(p3)
#print(p4)
#print(res)
print(p1==p1)
print(p1==p2)
print(p2*2)
print(2*p2)

class Sentence():

    def __init__(self, string=""):
        self.words_lst=string.split()

    def __str__(self):
        return str(self)

    def get_first_word(self):
        return self.words_lst[0]

    def get_all_words(self):
        return " ".join(self.words_lst)

    def replace(self, index, new_word):
        self.words_lst[index]=new_word

    def __lt__(self, other):
        return str(self<other)
        return self.words_lst<other.words_lst

s1=Sentence("I'm going back")
print(s1.get_all_words())
print(s1.get_first_word())
s1.replace(2, "home")
print(s1.get_all_words())

class WholeNumber():

    def __init__(self, val=0):
        if val>=0:
            self.val=val
        else:
            raise ValueError
    
    def __str__(self):
        return str(self.val)
        
    def __repr__(self):
        return str(self)

    def __add__(self, other):
        return WholeNumber(self.val+other.val)

    def __sub__(self, other):
        try:
            return WholeNumber(self.val-other.val)
        except ValueError:
            print("Not resulting a whole number.")

    def __mul__(self, other):
        return WholeNumber(self.val*other.val)

num1=WholeNumber()
print(num1)
num2=WholeNumber(2)
print(num2)
num3=WholeNumber(1)
print(num3-num2)
