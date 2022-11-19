#Euler 2
"""
    TODO:
   """
fib = [0]
counter = 0
lim = 4000000
i = 0
sol = 0

#Quick function to check if a number is  even
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


while fib[i] < lim:
    #If first in set, set value to 1
    if i == 0:
        fib.append(1)

    #If second in set, set value to 2
    elif i == 1:
        fib.append(2)

    #Otherwise, calculate fib[i] by adding fib [i - 1] and fib[i]
    else:
        fib.append(fib[i - 1] + fib[i])
        

    print(fib[i])
    if is_even(fib[i]):
        sol += fib[i]
    i += 1

print("The sum of all even numbers in the Fibonacci sequence less than 4 000 000 is: " + str(sol))
    










