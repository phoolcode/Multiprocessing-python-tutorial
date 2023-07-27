import time
from multiprocessing import Pool
from tqdm import tqdm

def slow_square(number):
    # Simulate a computationally inefficient task by adding a delay
    time.sleep(1)
    return number ** 2

if __name__ == "__main__":
    numbers = range(100)
    results = []

    progress_bar = tqdm(total=len(numbers), desc='Processing')

    with Pool() as pool:
        for item in pool.map(slow_square, numbers):
            results.append(item)

            # Update the progress bar
            progress_bar.update(1)
    # Close the progress bar
    progress_bar.close()
    print("Results with multiprocessing:", results)