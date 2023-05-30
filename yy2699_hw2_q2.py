def print_top (offset) :
    # signature: int -> NoneType
    print (offset * ' ' + '^')
def print_middle (offset , width) :
    # signature: int , int -> NoneType
    print (offset * ' ' + '/' + width * ' ' + '\\')
def print_bottom (offset , width):
    # signature: int , int -> NoneType
    print (offset * ' ' + width * '-')
"""offset indicates for how far of the output should be to the leftside,
and the width indicates for how far in print_middle() two signs of /\ should
be, as well as for how many in print_bottom sign - should be"""

def print_triangle():
    print_top(4)
    print_middle(3,1)
    print_middle(2,3)
    print_middle(1,5)
    print_bottom(1,7)
print_triangle()
