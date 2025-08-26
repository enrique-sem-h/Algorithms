def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if target == arr[middle]:
            return middle
        
        if target > arr[middle]:
            left = middle + 1

        if target < arr[middle]:
            right = middle - 1
    
    return -1

def recursiveBinarySearch(target, arr, left = 0, right = None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    middle = (left + right) // 2

    if target == arr[middle]:
        return middle
    elif target > arr[middle]:
        return recursiveBinarySearch(target, arr, middle + 1)
    elif target < arr[middle]:
        return recursiveBinarySearch(target, arr, left, middle - 1)

print(recursiveBinarySearch(7, [1, 2, 3, 4, 5, 6, 7, 8]))
print(binarySearch([1,2,3,4,5,6,7], 7))