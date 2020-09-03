def linear_search(arr, target):
    # Your code here
    if target in arr:
        return arr.index(target) 
    else:
        return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # create values to use
    start = 0
    middle = 0
    total = len(arr) - 1
    
    while start <= total:
        # find our middle index and use it as a starting point for the search (< or >)
        mid = (total + start) // 2
        # if the target > mid
        if arr[mid] < target:
            start = mid + 1

        # if the target < mid
        elif arr[mid] > target:
            total = mid - 1
        # if we got lucky and target is the mid
        else:
            return mid
    return -1  # not found
