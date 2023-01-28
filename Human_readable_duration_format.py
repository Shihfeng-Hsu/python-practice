def format_duration(seconds):
    years=0
    mons=0
    days=0
    hours=0
    mins=0
    time= []

    if seconds >= 31536000:
        years = int(seconds / 31536000)
        seconds = seconds % 31536000

    # if seconds >= 2592000:
    #      mons = int(seconds / 2592000)
    #      seconds = seconds % 2592000

    if seconds >= 86400:
        days = int(seconds / 86400)
        seconds = seconds % 86400
    
    if seconds >= 3600:
        hours = int(seconds / 3600)
        seconds = seconds % 3600

    if seconds >= 60:
        mins = int(seconds / 60)
        seconds = seconds % 60
    
    A= ((f"{years} years") if years>1 else (f"{years} year"))if years>0 else ""
    # B= ((f"{mons} months") if mons>1 else (f"{mons} month"))if mons>0 else ""
    C= ((f"{days} days") if days>1 else (f"{days} day"))if days>0 else ""
    D= ((f"{hours} hours") if hours>1 else (f"{hours} hour"))if hours>0 else ""
    E= ((f"{mins} minutes") if mins>1 else (f"{mins} minute"))if mins>0 else ""
    F= ((f"{seconds} seconds") if seconds>1 else (f"{seconds} second"))if seconds>0 else ""
    time=[A,C,D,E,F]
    filted_time = list(filter(None,time))
    if len(filted_time) == 0:
        print("now")
        return "now"
    str_part_one= ", ".join(filted_time[0:-1])
    str = str_part_one + " and " + filted_time[-1] if filted_time[-1] != "" and len(filted_time) > 1 else filted_time[-1]

    print(str)
    return str
    # return_str ={f"{years}{}"}

'''
Other solution - is more efficient than mine.

times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]'''


format_duration(0)#, "now")
format_duration(1)#, "1 second")
format_duration(62)#, "1 minute and 2 seconds")
format_duration(120)#, "2 minutes")
format_duration(3600)#, "1 hour")
format_duration(3662)#, "1 hour, 1 minute and 2 seconds")
format_duration(315360000)#, "10 years")
format_duration(458212571)#, "10 years")
'''
Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.


'''