import time

def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
# Sample list to be sorted
arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:")
print(arr)

start = time.time()
bubble_sort(arr)
elapsed = time.time() - start

print("Sorting time in milliseconds is: " + str(elapsed * 1000))
