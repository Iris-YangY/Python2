def convert_time ( time ):
    # sig : str -> str
    time=int(time)
    hour=time//100
    minute=time%100
    if hour>12:
        hour-=12
        hour=str(hour).zfill(2)
        if minute<10:
            minute=str(minute).zfill(2)
        output=print(hour,':',minute,'pm')
    elif hour<12 and hour!=0:
        hour=str(hour).zfill(2)
        if minute<10:
            minute=str(minute).zfill(2)
        output=print(hour,':',minute,'am')
    elif hour==12:
        if minute<10:
            minute=str(minute).zfill(2)
        output=print(hour,':',minute,'pm')
    else:
        hour=12
        if minute<10:
            minute=str(minute).zfill(2)
        output=print(hour,':',minute,'am')
    return output
convert_time("1227")
convert_time("0002")
convert_time("0102")
convert_time("1302")
