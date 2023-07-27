import time
import threading # importing threading module

complete = False
count = 0

def worker(count):
    while not complete:
    
        print("count = ", count)
        count = count + 1 

t1 = threading.Thread(target=worker, args=(count,)) # creating a thread called t1 using .Thread()

t1.start() # starting the thead

input("hit enter to exit loop\n")
complete = True