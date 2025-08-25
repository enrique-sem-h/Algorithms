def recursiveSum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recursiveSum(arr[1:])
    
def recursiveCount(arr):
    if len(arr) == 1:
        return 1
    else:
        return 1 + recursiveCount(arr[1:])
    
def recursiveHighest(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], recursiveHighest(arr[1:]))
    

def binarySearch(target, arr, left = 0, right = None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    middle = (left + right) // 2

    if target == arr[middle]:
        return middle
    elif target > arr[middle]:
        return binarySearch(target, arr, middle + 1)
    elif target < arr[middle]:
        return binarySearch(target, arr, left, middle - 1)

print(binarySearch(10, [1,2,3, 4, 5, 6, 7, 8]))

# print(recursiveCount([1, 2, 3, 4]))
# print(recursiveHighest([3, 5, 4, 2]))