import math
import time
start_time = time.time() 

def get_num_factors(n):
    """
        Returns the total number of positive factors of n

        1) Define the mirror line (Where factors begin their opposites)
        2) Test each number from 1 to the mirror line
        3) If a factor is found, increase factors by 2 (itself and it's counterpart)
        4) Return the total number of factors.
    """
    if n == 1:
        return 1
    #elif is_prime(n):
    #    return 2

    lim = int(math.sqrt(n)) + 1
    factors = 2

    for i in range(2, lim):
        if n % i == 0:
            factors += 2

    return factors

def print_factors(n):
    """
        Prints all of the positive factors of a number
        Uses the same mirror-line technique
        Uses two strings, one to store the ascending factors
        One to store the decendending factors
        Joints the strings then prints 
    """
    lim = int(math.sqrt(n)) + 1
    factors_1 = "Factors: "
    factors_2 = ""
    for i in range(1, lim):
        if n % i == 0:
            factors_1 += str(i) + ","
            factors_2 = "," + str(int(n/i)) + factors_2
            
    factors = factors_1 + factors_2[1:]
    print(factors)


factors = 1
triangle_number = 0
iterator = 1

while factors <= 500:
    triangle_number += iterator
    factors = get_num_factors(triangle_number)
    iterator += 1   

print("Triangle number:",int(iterator),"\nValue:",int(triangle_number))
print_factors(triangle_number)

print("--- %s seconds ---" % (time.time() - start_time))

