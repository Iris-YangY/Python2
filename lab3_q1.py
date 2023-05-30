def func_a (x , y ):
    return y ** x
print ( func_a (5 , 3))
print ( func_a (2 , 5))
print ( func_a (3 , 3))

def func_b (x , y , z ):
    return str ( x ) + str ( y ) * z
print ( func_b (1 ,2 ,3))
print ( func_b (12 ,34 ,5))
print ( func_b (3 ,2 ,1))
print ( func_b (3 ,2 ,0))

def func_c ( x ):
    return x - 4
def func_c1 ( x ):
    return func_c ( x ) * 2
def func_c2 ( x ):
    return func_c1 ( x ) + 5
print ( func_c2 (7))

def func_d ( x ):
    x = x - 5
    y = x ** 2
    return y
def main ():
    x = 10
    y = func_d ( x )
    print ( y )
main ()

def make_odd ( n ):
    return 2 * n + 1
print ( make_odd (2))
n = 3
print ( make_odd ( n ))
print (1 + make_odd (3))
