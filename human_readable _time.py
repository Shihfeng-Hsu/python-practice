def make_readable(seconds):
    secs=seconds%60
    mins=int((seconds-secs)%3600/60)
    hours=int(seconds/3600)
    if hours<10:
        hours=f'0{hours}'
    if mins <10:
        mins=f'0{mins}'
    if secs <10:
        secs=f'0{secs}'
    print(f'{hours}:{mins}:{secs}')
    return f'{hours}:{mins}:{secs}'
 
# def make_readable(s):
#     return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

make_readable(0) #, "00:00:00")
make_readable(5) #, "00:00:05")
make_readable(60) #, "00:01:00")
make_readable(86399) #, "23:59:59")
make_readable(359999) #, "99:59:59")