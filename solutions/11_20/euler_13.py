import time
start_time = time.time()

temp_num = ""
temp_list = []
nums = []
char = "0"
total = 0

with open(r'C:\Users\jorda\source\repos\Euler-3.0\solutions\11_20\euler_13_number.txt') as _file:
    while char != "":
        #Read one char at a time
        char = _file.read(1)

        if char == "\n" or char == "":
            temp_list.append(int(temp_num))
            temp_num = ""
            nums.append(temp_list)
            temp_list = []                    
        
        temp_num += char       

for num in nums:
    total += num[0]

string = str(total)
print(string[0:10])

print("--- %s seconds ---" % (time.time() - start_time))
