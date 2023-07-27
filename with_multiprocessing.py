# Speeding up the code using multiprocessing
import time
import multiprocessing

def standup(updates, no_of_members):
    """
    simulates a stand-up meeting by iterating over the range of `no_of_members` 
    and printing `updates` by introducing a 1-second delay between each update

    """
    for i in range(no_of_members):
        print(updates, i)
        time.sleep(1)

def work(task, no_of_tasks):
    """
    simulates a work task by iterating over the range of `no_of_tasks` 
    and printing `task` by introducing a 1.5-second delay between execution of each task
    """
    for i in range(no_of_tasks):
        print(task, i)
        time.sleep(1.5)

def coffee():
    """
    simulates a coffee break of 3 seconds
    """
    time.sleep(10)
    print("coffee break is done")

if __name__ == "__main__":
    updates = "The update is being given by attendee no. "
    task = "Task being completed is at priority "

    start_time = time.time()

    # spawning up individual 
    t1 = multiprocessing.Process(target=standup,args=(updates, 4))
    t2 = multiprocessing.Process(target=work,args=(task, 3))
    t3 = multiprocessing.Process(target=coffee)

    # starting the processes
    t
    t2.start()
    t3.start()

    # wait until process 1 is finished
    t1.join()
    t2.join()
    t3.join()

    print("It's time to go home")
    print("time required = ", time.time() - start_time )