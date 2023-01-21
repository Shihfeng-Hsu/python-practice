def solution(s):
  splitPoint=[0]
  splitArr=[]
  for i in range(0,len(s)):
    if s[i].isupper() == True :
      splitPoint.append(i)
  splitPoint.append(-1)
  for i in range(0,len(splitPoint)-1):
    if i == len(splitPoint)-2:
        string= s[splitPoint[i] : splitPoint[i+1]]+s[-1]
    else:
        string= s[splitPoint[i] : splitPoint[i+1]]
    splitArr.append(string)
    print(string)
  print(splitArr)
  print(" ".join(splitArr))
  return " ".join(splitArr)

#solution 1
# def solution(s):
#     return ''.join(i if i.islower() else ' ' + i for i in s)

#solution 2
# import re
# def solution(s):
#     return re.sub(r'([A-Z])', r' \1', s)

solution("helloWorld") #hello World