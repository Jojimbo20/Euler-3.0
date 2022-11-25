"""
    Euler 10:
        The sum of the primes below 10 is:
        2 + 3 + 5 + 7 = 17

        Find the sum of the primes below 2 000 000 
"""
"""
    This is a very easy solution to brute force but might take a while
    Test numbers below 2 000 000 for primality
    If prime then add to sum.

    When complete show the sum
"""

import time
import math
start_time = time.time()



def is_prime(n):
    #Two is prime
    if (n == 2):
        return True
    #Zero and one aren't prime, if a number is even then it's not prime
    elif (n == 0) or (n == 1) or (n % 2 == 0):
        return False

    #Since we have excluded (0, 1, 2, 4, 6, 8)
    #The remaining numbers less than 9 are all primal (3,5,7)
    elif n < 9:
        return True

    #Get the factor mirror line 
    lim = int(math.sqrt(n)) + 1

    #Iterate up to the mirror line testing for factors.
    for i in range(3, lim, 2):
        #If a factor is found, return False. 
        if n % i == 0:
            return False
    #If no factors are found the number is Prime
    return True


#Starting at 2 because for loop later starts at 3
_sum = 2
target_num = 2000000

#Check if each odd number upto the target is prime
for i in range(3,target_num,2):

    #If it is add it to the cumulative sum
    if is_prime(i):
        _sum += i

print("Sum of all primes below 2 million is: {_s}".format(_s=_sum))
print("--- %s seconds ---" % (time.time() - start_time))