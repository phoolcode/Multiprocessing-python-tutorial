import threading
import time

complete = False
count = 0

def worker(count):
    while not complete:
        time.sleep(1)
        print("count = ", count)
        count = count + 1 

worker(count)

input("hit enter to exit loop")
complete = True