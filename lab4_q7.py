def is_triangle (a , b , c ):
    # sig : int , int , int -> bool
    if a>=b:
        short=b
        longer=a
        if a>=c:
            longer=c
            longest=a
        else:
            longest=c
    elif a<=b:
        short=a
        longer=b
        if b>=c:
            longer=c
            longest=b
        else:
            longest=c
    if short+longer>longest:
        if longer-short<longest:
            output="True"
        else:
            output="False"
    else:
        output="False"
    return output
print(is_triangle(3,4,5))
print(is_triangle(5,3,4))
print(is_triangle(4,5,3))
print(is_triangle(2,2,4))
print(is_triangle(4,2,2))
print(is_triangle(2,4,2))
