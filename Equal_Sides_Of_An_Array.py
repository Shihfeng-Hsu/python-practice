def find_even_index(arr):
    for i in range(len(arr)):
        a=0
        b=0
        index=[]
        for j in range(0,i):
            a += arr[j]
        for j in range(i+1,len(arr)):
            b += arr[j]
        if a == b:
            index.append(i)
            print(index[0])
            return index[0]
    print(-1)
    return -1
    

    #your code here

'''

other solution

def find_even_index(lst):
    left_sum = 0
    right_sum = sum(lst)
    for i, a in enumerate(lst):
        right_sum -= a
        if left_sum == right_sum:
            return i
        left_sum += a
    return -1

'''


find_even_index([1,2,3,4,3,2,1])#,3)
find_even_index([1,100,50,-51,1,1])#,1,)
find_even_index([1,2,3,4,5,6])#,-1)
find_even_index([20,10,30,10,10,15,35])#,3)
find_even_index([20,10,-80,10,10,15,35])#,0)
find_even_index([10,-80,10,10,15,35,20])#,6)
find_even_index(list(range(1,100)))#,-1)
find_even_index([0,0,0,0,0])#,0,"Should pick the first index if more cases are valid")
find_even_index([-1,-2,-3,-4,-3,-2,-1])#,3)
find_even_index(list(range(-100,-1)))#,-1)