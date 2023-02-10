from math import lcm
from functools import reduce
def convert_fracts(lst):
    if len(lst) == 0 :
        return lst
    secondary_num = []
    for item in lst:
        secondary_num.append(item[1])
    
    biggest_num = reduce(lcm,secondary_num)
  
    for item in lst:
        times = int(int(biggest_num) / int(item[1]))
        item[0] = int(int(item[0]) * times)
        item[1] = int(biggest_num)
    
    print(lst)
    return lst

'''
    #gcd solution by cause timeout....
    #just use the math method will be good
    #  secondary_num.sort(reverse=True)
    # bigest_num =secondary_num[0]
    # while True:
    #     a = 0 
    #     for i in secondary_num:
    #         a = bigest_num % i
    #         if a != 0:
    #             break
    #     if a == 0:
    #         break
    #     else:
    #         bigest_num = bigest_num + secondary_num[0]
'''









        



a = []
b = []
convert_fracts(a)#, b)
a = [[1, 2], [1, 3], [1, 4]]
b = [[6, 12], [4, 12], [3, 12]]
convert_fracts(a)#, b)


'''
Common denominators

You will have a list of rationals in the form

{ {numer_1, denom_1} , ... {numer_n, denom_n} } 
or
[ [numer_1, denom_1] , ... [numer_n, denom_n] ] 
or
[ (numer_1, denom_1) , ... (numer_n, denom_n) ] 
where all numbers are positive ints. You have to produce a result in the form:

(N_1, D) ... (N_n, D) 
or
[ [N_1, D] ... [N_n, D] ] 
or
[ (N_1', D) , ... (N_n, D) ] 
or
{{N_1, D} ... {N_n, D}} 
or
"(N_1, D) ... (N_n, D)"
depending on the language (See Example tests) in which D is as small as possible and

N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
Example:
convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]
Note:
Due to the fact that the first translations were written long ago - more than 6 years - these first translations have only irreducible fractions.

Newer translations have some reducible fractions. To be on the safe side it is better to do a bit more work by simplifying fractions even if they don't have to be.

Note for Bash:
input is a string, e.g "2,4,2,6,2,8" output is then "6 12 4 12 3 12"


'''