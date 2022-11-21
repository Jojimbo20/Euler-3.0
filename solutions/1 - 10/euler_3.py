#Euler 3
import time
import math
start_time = time.time()

#is_prime(n) : Checks if a number is Prime | Returns: True, False
""" ..............................................................................................
    ...To check if a number is prime, we only need to check up to the square root of the number...
    ..............................................................................................
    Brute Force Method up to Sqrt(N) | Time Complexity: ?
    
    1) Iterates through all numbers from 3 to sqrt(n) (since the sqrt represents the "Mirror" line)        
    2) Checks to see if the iteration is a factor of n
    3) If a factor is found, the number is not prime
    4) Otherwise the number is prime
"""
def is_prime(n):

    #Does a quick check to see if the number is 1 or divisible by 2
    if n == 1 or n % 2 == 0:
        return False

    #Defines upper limit for testing
    lim = int(math.sqrt(n))

    #Iterates from 3 up to the square root of n only checking odd numbers as the product of a number and any even number is always an even number
    #If it finds a factor that is between 3 and the square root then the number is not prime
    for num in range(3, lim, 2):
        if n % num == 0:            
            return False
    
    #If the function doesn't find any factors between 2 and the square root then the number is prime
    return True

target_num = 600851475143
largest_prime_factor = 0

#Quick check to see if target_num is prime
if is_prime(target_num):
    largest_prime_factor = target_num
    print("The largest prime factor of " + str(target_num) + " is: " + str(largest_prime_factor))
    print("--- %s seconds ---" % (time.time() - start_time))
    exit()

#i Iterates from 2, up to half of the target number, as there are no factors > target_num/2
#Divides target_number by i, giving the largest possible factor then checks if that factor:
#Is odd? (Prevents unneccesary checking of even numbers)
#Is prime?
#if all conditions are met then largest prime number has been found.
i = 2;
while i < int(target_num/2):
    if target_num % i == 0 and (target_num / i) % 2 != 0 and is_prime(target_num/i):
        largest_prime_factor = target_num / i
        break
    i += 1

#No prime factor has been found
if largest_prime_factor == 0:
    print(str(target_num) + " doesn't have any prime factors.")

#Print the largest prime factor
else:
    print("The largest prime factor of " + str(target_num) + " is: " + str(int(largest_prime_factor)))

print("--- %s seconds ---" % (time.time() - start_time))
