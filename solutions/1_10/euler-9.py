"""
    Euler 9:
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:
                        a^2 + b^2 = c^2

               Example: 3^2 + 4^2 = 5^2
                          9 + 16  = 25

    There exists exactly one Pythagorean triplet for which a + b + c = 1000
    find the product abc
"""

"""
    This is one of those problems where I feel like there's definitely a mathsy way of working out a good solution
    For complexity, I managed to work out a way to calculate the number of possible solutions to a + b + c = x

    My approach is:

    Create an algorithm to generate the complete list of possible solutions to a + b + c = desired_sum
    Then check each solution to see if the following equation is true:
    a*a + b*b = c*c
"""
"""
    Input desired_sum of the three variables
    Set c to the sum - 3 (number of variables)
    b = 2
    a = 1

    while a < b and b < c:
        if condition is met:
            done

        increment b by 1
        decrement c by 1
        
        if c <= b then the condition b < c is no longer valid:
            decrease the upper limit of c by 2 (num of variables - 1)
            increment a by 1 
            set b to a + 1
"""
#Solution:
import time
start_time = time.time()

#c_lim represents the number c starts at
desired_sum = 1000
c_lim = desired_sum - 3
a = 1
b = 2
c = c_lim
combinations = 0


while a < b and b < c:
    #This just prints the possible solutions to a + b + c = desired_sum 
    #Comment out to improve performance
    print("{_a} + {_b} + {_c} = {_ans}".format(_a=a,_b=b,_c=c,_ans=(a+b+c)))

    #Solution has been found
    if (a*a + b*b) == c*c:        
        print("\nSolution found:")
        print("{_a}^2 + {_b}^2 = {_c}^2".format(_a=a,_b=b,_c=c),"\n")
        print("{_a} * {_b} * {_c} = {_ans}".format(_a=a,_b=b,_c=c,_ans=(a*b*c)))
        input("\nProgram paused, hit enter to contiue. ")   
    
    #If the conditions haven't been met, increment to check another solution
    b += 1
    c -= 1
    combinations += 1

    #If c isn't greater than b anymore, it's no longer a valid solution, 
    #Increment a by 1, set be to a + 1 to satisfy a < b and set c to limit - 2 to start a new round of checking
    if c <= b:
        c_lim -= 2
        c = c_lim
        a += 1
        b = a + 1
#print("There are", combinations, "possible combinations of a + b + c = {_t} where a < b < c".format(_t=target_num))

print("--- %s seconds ---" % (time.time() - start_time))