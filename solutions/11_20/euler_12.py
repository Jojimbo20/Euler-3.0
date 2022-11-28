import math
import time
start_time = time.time() 

def get_num_factors(n):
    if n == 1:
        return 1
    elif is_prime(n):
        return 2

    lim = int(n/2) + 1
    factors = 2

    for i in range(2, lim):
        if n % i == 0:
            factors += 1

    return factors

def get_num_factors_2(n):
    if n == 1:
        return 1

    lim = int(n/2) + 1
    factors = 1
    product = 1

    for i in range(2, lim):
        if n % i == 0:
            factors += 1
            product *= i
            if product == n:
                break
            elif n % product == 0:
                factors += 1
    return factors

def print_factors(n):
    lim = int(n/2) + 1
    factors = "Factors:"
    for i in range(1, lim):
        if n % i == 0:
            factors += str(i)
            factors += ","

    print(factors)

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

factors = 1
running_total = 0
iterator = 1

while factors <= 10:
    running_total += iterator
    factors = get_num_factors_2(running_total)
    iterator += 1   

print("Triangle number:",int(iterator),"\nValue:",int(running_total))
print_factors(running_total)

print("--- %s seconds ---" % (time.time() - start_time))

