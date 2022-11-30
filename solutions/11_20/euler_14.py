import time
start_time = time.time()

#Collatz sequence
longest_chain = []

for i in range(2,1000000):
    working_chain = [i]

    n = i
    while n != 1:
        if n % 2 == 0:
            n = int(n/2)
            working_chain.append(n)

        elif n % 2 != 0:
            n = (3 * n) + 1
            working_chain.append(n)
    if len(working_chain) > len(longest_chain):
        longest_chain = working_chain

print(str(longest_chain[0]))

print("--- %s seconds ---" % (time.time() - start_time))


