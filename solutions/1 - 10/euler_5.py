"""
    EULER 5: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest possible number evenly divisible by all numbers from 1 to 20?
"""
import time
start_time = time.time()

working_num = 2520
i = 2

while i <= 20:
    if working_num % i !=0:
        working_num += 20
        i = 1
    i += 1

print("Smallest number divisible by all numbers from 1 to 20 is: {Answer}".format(Answer=working_num))
print("--- %s seconds ---" % (time.time() - start_time))