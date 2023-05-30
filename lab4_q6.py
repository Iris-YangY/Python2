def calculate_price ( item1 , item2 , card , tax_rate ):
    # sig : float , float , bool , float -> float
    if item1<item2:
        total=item2+0.5*item1
        if card==True:
            total=total*0.9
        else:
            total=total
        total=total*(1+tax_rate/100)
    else:
        total=item1+0.5*item2
        if card==True:
            total=total*0.9
        else:
            total=total
        total=total*(1+tax_rate/100)
    return total
print(calculate_price(10,20,True,8.25))
print(calculate_price(20,10,False,8.25))
print(calculate_price(20,20,False,5.0))
