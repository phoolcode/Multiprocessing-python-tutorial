import time
from multiprocessing import Pool, cpu_count

def create_and_save_file_map(string_info):
    i, string = string_info
    file_name = f"file_{i+10}.txt"
    time.sleep(2)
    with open(file_name, "w") as file:
        file.write(string)
    return file_name

if __name__ == "__main__":
    strings = [
        "Abhijit",
        "Anas",
        "Ayush",
        "Falguni",
        "Harjot",
        "Jigyasa",
        "Prachi",
        "Saurabh",
        "Sheshant",
        "Rahul"
    ]
    start_time = time.time()


    # Using multiprocessing pool with worker processes = the number of core available on the os
    with Pool(processes=cpu_count()) as pool:
        for item in pool.map(create_and_save_file_map, enumerate(strings)):
            print(f"file {item} created")

    pool.close()

    print("time required =", time.time() - start_time)