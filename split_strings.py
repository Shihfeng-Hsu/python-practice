def solution(s):
    arr=[]
    i=0
    while i < len(s)-1:
        arr.append(s[i]+s[i+1])
        i+=2
    if len(s)%2 != 0:
        arr.append(f"{s[-1]}_")
    print(arr)
    return arr


# def solution(s):
#     result = []
#     if len(s) % 2:
#         s += '_'
#     for i in range(0, len(s), 2):
#         result.append(s[i:i+2])
#     return result
# This is the more efficient solution by using for range loop.
# Just like a JS for loop : for(let i = 0, i < s.length, i++)

solution("zaqxswcde") #['za', 'qx', 'sw', 'cd', 'e_']
solution("ABC")#['AB', 'C_']