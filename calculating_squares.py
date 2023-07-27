import time

def calc_square(i):
   return i*i
    
list_of_nums = [1, 2, 3, 4, 5]
result_list = []

t1 = time.time()
for i in list_of_nums:
   result_list.append(calc_square(i))

print("The list of squares = ", result_list)
print("time required =", time.time() - t1)