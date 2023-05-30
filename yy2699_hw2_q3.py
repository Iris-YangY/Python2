def double (n) :
    # signature: int -> int
    # return doubled value of parameter
    return n * 2
def succ (n) :
    # signature: int -> int
    # returns successor of parameter
    return n + 1
def f (n) :
    # signature: int -> int
    # returns the value 2*n + 1
    n=double(n)
    n=succ(n)
    return n
def g (n) :
    # signature: int -> int
    # returns the value 4*n
    n=double(n)
    n=double(n)
    return n
def h (n) :
    # signature: int -> int
    # returns the value 8*n + 4
    n=g(n)
    n=f(n)
    n=succ(n)
    n=succ(n)
    n=succ(n)
    return n
print(g(1))
print(h(2))
