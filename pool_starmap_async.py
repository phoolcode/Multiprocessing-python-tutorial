import time
from multiprocessing import Pool, cpu_count

def create_and_save_file_starmap(string_info, time_out):
    i, string = string_info
    file_name = f"file_{i+40}.txt"
    time.sleep(time_out)
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
    time_out = [1, 2, 3, 1, 2, 3, 1, 2, 3, 2]
    start_time = time.time()

    # prepare arguments
    input_tuples = list(zip(enumerate(strings), time_out))

    print(input_tuples)
    
    # Using multiprocessing pool with worker processes = the number of core available on the os
    with Pool(processes=cpu_count()) as pool:
        # Use map_async instead of map
        result_async = pool.starmap_async(create_and_save_file_starmap, input_tuples)
        print("Other work while waiting for function calls to complete...")

        # blocking call using get()
        results = result_async.get()

        for item in results:
            print(f"file {item} created")

    pool.close()

    print("time required =", time.time() - start_time)