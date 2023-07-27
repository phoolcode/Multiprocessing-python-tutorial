import time
from multiprocessing import Pool

def create_and_save_file_apply(file, string):
    """
    creates and saves a single file with the given filename and content string
    """
    file_name = f"file_{file}.txt"
    time.sleep(2)        
    with open(file_name, "w") as file:
        file.write(string)
    return file_name

 
# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    pool = Pool()
    # issue tasks to the process pool
    result = pool.apply(create_and_save_file_apply, args=("empid_27468", "Falguni"))
    # report value
    print(result, "created")
    # close the process pool
    pool.close()