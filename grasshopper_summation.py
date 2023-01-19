###################
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
# For example (Input -> Output):
# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
####################

def summation(num):
    sum=0
    i=1
    while i <=num:  #while statement
        sum+=i
        i+=1        #while statement
    print(sum)
    return sum

#The same as :
# function summation(num){
#     let sum=0;
#     for(let i=0; i<num; i++){
#         sum += i
#     }
#     return sum
# }

summation(321)