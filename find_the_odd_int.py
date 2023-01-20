def find_it(seq):
    countArr=[]
    for i in seq:
        if countArr.count(i)==0:
            countArr.append(i)
    for i in countArr:
        if seq.count(i)%2 !=0:
            print(i)
            return i

# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i
# This approch is more efficient than I did.

find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) # should return 5 (because it appears 3 times)")
find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]) #should return 5 (because it appears 3 times)")
