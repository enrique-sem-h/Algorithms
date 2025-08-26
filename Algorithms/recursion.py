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
    

# print(recursiveCount([1, 2, 3, 4]))
# print(recursiveHighest([3, 5, 4, 2]))