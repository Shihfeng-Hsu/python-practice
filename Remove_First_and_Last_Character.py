def remove_char(s):
    arr = []

    for chr in s:
        arr.append(chr)
    print("".join(arr[1:-1]))
    return "".join(arr[1:-1])


'''
other solution:

def remove_char(s):
    return s[1 : -1]
    
# Using the string index will easily pass the test.
# My solution may be more complicated, but some languages don't support string indexes, so to solve it you must use array method.



'''


remove_char('eloquent')#, 'loquen')
remove_char('country')#, 'ountr')
remove_char('person')#, 'erso')
remove_char('place')#, 'lac')
remove_char('ok')#, '')
remove_char('ooopsss')#, 'oopss')