def find_smallest_int(arr):
  # return sorted(arr)[0]
  arr.sort()
  
  print(sorted(arr))# A
  print(arr)# B
  # the code line A is the same as the code line B.

  arr.sort(reverse=True)# C
  print(arr)# C
  
  return arr

find_smallest_int([1,3,9,-110])