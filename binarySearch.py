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

print(binarySearch([1,2,3,4,5,6,7], 10))