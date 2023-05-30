def is_leap_year (year):
    """
    sig : int -> bool
    """
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False
def days_in_month (month, year):
    # sig : int , int -> int
    
    if month==(1 or 3 or 5 or 7 or 8 or 10 or 12):
        output=31
    else:
        if month==(4 or 6 or 9 or 11):
            output=30
        else:
            if month==2:
                if is_leap_year(year)==True:
                    output=29
                else:
                    output=28
    return output
print(days_in_month(1,2019))
print(days_in_month(2,2018))
print(days_in_month(2,2000))
