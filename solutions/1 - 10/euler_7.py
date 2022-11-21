"""
    Euler 7
    By listing the first 6 prime numbers, 2, 3, 5, 7, 11, 13 we can see that the 6th prime number is 13
    
    What is the 10 001st prime number?
"""

"""
    Create a list to store primes
    For each prime number add to the list add one to the counter 
    Return last element
"""

#Solution:
import math

def is_prime(p):
    #Prime numbers can't be even
    if p % 2 == 0:
        return False

    #When testing a number for primality, we only need to test upto the mirror line (square root of the number)
    lim = int(math.sqrt(p))

    for i in range(3, lim+1, 2):
        if p % i == 0:
            return False

    return True    


#To make life easier, I've added the first two primes
primes = [2,3]
position = 10001

#p is our variable we will use to generate numbers to test
p = 5
while len(primes) <= position:
    if is_prime(p):
        primes.append(p)
    p += 2

print("10001st prime number is: {p}".format(p=primes[-1]))