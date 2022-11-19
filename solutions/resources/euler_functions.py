import math

def test_import():
    print("You successfully imported from euler_functions.py!")

def is_even(x):
    if x % 2 == 0:
        return True
    return False

def is_prime(n):
    #Does a quick check to see if the number is 1 or divisible by 2
    if n == 1 or n % 2 == 0:
        return False

    #Defines upper limit for testing
    lim = int(math.sqrt(n))

    #Iterates from 3 up to the square root of n only checking odd numbers as the product of a number and any even number is always an even number
    #If it finds a factor that is between 3 and the square root then the number is not prime
    for num in range(3, lim):
        if n % num == 0:            
            return False
    
    #If the function doesn't find any factors between 2 and the square root then the number is prime
    return True

def is_palindrome(n): 
    if reverse_num(abs(n)) != n:
        return False
    return True

def reverse_num(n):
    try:
    #i is used to store the number of individual digits in n
    #The temp_list is initialised with 0 as place holders 
        i = len(str (n))
        temp_list = [0] * i   

    
    #Take each individual digit (Starting from the left of the number) and set it to the last place of the list
    #Move backwards assigning the values
        for c in str(n):
            
                temp_list[i - 1] = int(c)
                i -= 1;
    except Exception as e:
        print("Error: {error}, did you pass a float to is_palindrome(int)?".format(error=e))    
        quit() 

    return list_to_num(temp_list)

def list_to_num(l):
    num = ''.join(map(str,l))
    return int(num)