"""
    Euler 6:
    The sum of the squares of the first ten natural numbers is,
    1*1 + 2*2 + ... 10*10 == 385

    the square of the sum of the first ten natural numbers is,
    (1+2+...10)^2 == 55^2 == 3025

    The difference between the sum of the squares and the square of the sum is:
    3025 - 385 == 2640


    Find the difference between the sum of the squares of the first 100 natural numbers
    and the square of the sum. 
"""
import time
start_time = time.time()

target = 100

i = 1 
sum_of_nums = 0

while i <= target:
    sum_of_nums += i
    i += 1

square_of_sum = sum_of_nums * sum_of_nums

i = 1
sum_of_squares = 0
while i <= target:
    sum_of_squares += i*i 
    i += 1

ans = abs(sum_of_squares - square_of_sum)

print("The difference between the sum of the squares of the first 100 natural numbers and the square of the sum is: {a}".format(a=ans))
print("--- %s seconds ---" % (time.time() - start_time))