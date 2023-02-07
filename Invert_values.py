def invert(lst):
    arr =[]
    for item in lst:
        arr.append(item * -1)
    print(arr)
    return arr
    pass


'''
The better solution

def invert(lst):
    return [-x for x in lst]
'''

invert([1,2,3,4,5])#,[-1,-2,-3,-4,-5])
invert([1,-2,3,-4,5])#, [-1,2,-3,4,-5])
invert([])#, [])