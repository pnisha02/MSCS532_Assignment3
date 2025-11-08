import random
import time
# Randomized Quicksort

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x > pivot]
    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)

def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # first element as pivot
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)

# Compare algorithms with different examples

def compare_sorting_algorithms():
    sizes = [10, 15, 20]  # smaller sizes for demonstration
    distributions = {
        "random_small": lambda n: [random.randint(1, 50) for _ in range(n)],
        "sorted_small": lambda n: list(range(1, n+1)),
        "reverse_small": lambda n: list(range(n, 0, -1)),
        "repeated_small": lambda n: [random.choice([2, 5, 7, 10]) for _ in range(n)]
    }

    for dist_name, generator in distributions.items():
        print(f"\nDistribution: {dist_name}")
        for size in sizes:
            arr = generator(size)
            arr_copy = arr.copy()
            
            start = time.time()
            randomized_quicksort(arr)
            rand_time = time.time() - start
            
            start = time.time()
            deterministic_quicksort(arr_copy)
            det_time = time.time() - start

            print(f"Size: {size:2d} | Array: {arr_copy}")
            print(f"Randomized QS Time: {rand_time:.6f}s | Deterministic QS Time: {det_time:.6f}s")


# Run the comparison
if __name__ == "__main__":
    compare_sorting_algorithms()
