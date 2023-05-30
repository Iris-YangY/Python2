def x(y):
    print(y * 2)
    return y + 1
def q(v, z):
    z = x(z)
    w = z + x(v)
    print(w)
q(30, 5)
#10
#60
#37

def c():
    print("C")
def b():
    print("B1")
    c()
    print("B2")
def a():
    print("A1")
    b()
    print("A2")
a()
"""
A1
B1
C
B2
A2
"""
def second(s):
    s = s +"!"
    return s
def first(s):
    return second(s) + second(s)
print(first("Ok"))

"""Ok!Ok!"""

