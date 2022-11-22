"""
    EULER 4:
    A palindromic number reads the same both ways,
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99    

    Find the largest palindrome made from the product of two 3-digit numbers.
"""

#Function to check if n is palindrome 
#Can't handle floats
#Needs error handling
def is_palindrome(n): 
    if reverse_num(abs(n)) != n:
        return False
    return True

#Function to reverse a number, returns the reverse of n as an int
#Needs error handing.
#Can't handle floats as of right now
#Can't handle negative numbers
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

#Quick function converts a list of ints into a single int
#Needs error handling
def list_to_num(l):
    num = ''.join(map(str,l))
    return int(num)

"""
    Program layout

    Set lower and upper limits 
    Iteration through all possible products within the limits
    Is the product larger than the current palindrome?
    Is the product a palindrome?
    Return largest palindrome
"""

largest_palindrome = 0
lower_lim = 100
upper_lim = 1000
p1 = 1
p2 = 1
products = [0] * 2

while p2 < upper_lim:
    p1 = lower_lim
    while p1 < upper_lim:
        if (p1*p2) > largest_palindrome and is_palindrome(p1*p2):
            largest_palindrome = p1*p2
            products[0] = p1
            products[1] = p2
        p1 += 1
    p2 += 1

print("The largest possible palindrome as a product of two three digit numbers is: {p1} * {p2} = {lp}".format(p1=products[0], p2=products[1], lp=largest_palindrome))