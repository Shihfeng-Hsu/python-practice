from math import sqrt
def is_prime(n):
    if n < 0:
        return False
    if n == 0:
        return False    
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

is_prime(0)#  False, "0  is not prime")
is_prime(1)#  False, "1  is not prime")
is_prime(2)#  True, "2  is prime")
is_prime(73)# True, "73 is prime")
is_prime(75)# False, "75 is not prime")
is_prime(-1)# False, "-1 is not prime")

    
  