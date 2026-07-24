import random
import time

# -------------------------------
# Interpolation Search Function
# -------------------------------
def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high and key >= arr[low] and key <= arr[high]:
        if low == high:
            if arr[low] == key:
                return low
            return -1

        # Estimate the position
        pos = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == key:
            return pos
        elif arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# -------------------------------
# Binary Search Function
# -------------------------------
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# -------------------------------
# Performance Analysis
# -------------------------------
sizes = [1000, 10000, 100000, 500000]

print("{:<10} {:<20} {:<20}".format("Size", "Interpolation(s)", "Binary(s)"))

for size in sizes:

    # Create sorted array
    arr = list(range(size))

    # Random key
    key = random.randint(0, size - 1)

    # Measure Interpolation Search
    start = time.perf_counter()
    interpolation_search(arr, key)
    interpolation_time = time.perf_counter() - start

    # Measure Binary Search
    start = time.perf_counter()
    binary_search(arr, key)
    binary_time = time.perf_counter() - start

    print("{:<10} {:<20.10f} {:<20.10f}".format(
        size,
        interpolation_time,
        binary_time
    ))
