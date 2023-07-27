import time
from multiprocessing import Pool, cpu_count

def create_and_save_file_map(string_info):
    i, string = string_info
    file_name = f"file_{i+30}.txt"
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

    with Pool(processes=cpu_count()) as pool:
        result_async = pool.map_async(create_and_save_file_map, enumerate(strings))
        print("Other work while waiting for function calls to complete...")

        # Get the results using get() (blocking call)
        results = result_async.get()

        for item in results:
            print(f"file {item} created")

    print("Time required =", time.time() - start_time)
