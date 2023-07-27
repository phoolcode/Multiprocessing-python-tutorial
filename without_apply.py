import time
from multiprocessing import Pool

def create_and_save_files(file, string):
    file_name = f"file_{file}.txt"
    time.sleep(2)        
    with open(file_name, "w") as file:
        file.write(string)
    return file_name
    

res = create_and_save_files("empid_27468", "Falguni")
print(res, "created")