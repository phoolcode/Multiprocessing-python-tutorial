import time

def create_and_save_files(string_array, timeout):
    for i, string in enumerate(string_array):
        file_name = f"file_{i+1}.txt"
        time.sleep(time_out[i])
        with open(file_name, "w") as file:
            file.write(string)

if __name__ == "__main__":
    # Array of 10 strings
    strings = [
        "Abhijit",
        "Anas",
        "Ayush",
        "Falguni",
        "Harjot",
        "Jigyasa",
        "Prachi"
        "Saurabh",
        "Sheshant",
        "Rahul"]
    time_out = [1, 2, 3, 1, 2, 3, 1, 2, 3, 2]
    start_time = time.time()
    create_and_save_files(strings, time_out)
    print("time required = ", time.time() - start_time )