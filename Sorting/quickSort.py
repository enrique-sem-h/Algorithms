import random

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    index = random.choice(arr)
    pivot = arr[index]
    smallest = [i for i in arr if i < pivot]
    equals = [i for i in arr if i == pivot]
    biggest = [i for i in arr if i > pivot]

    return quickSort(smallest) + [pivot] + quickSort(biggest)

print(quickSort([9, 3, 1, 4, 2, 5, 7, 6, 8]))

