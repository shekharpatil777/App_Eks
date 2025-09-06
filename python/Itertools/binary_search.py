# Linear search
def linear_search(arr, x):
    for i, val in enumerate(arr):
        if val == x:
            return i
    return -1
print(linear_search([1,2,3,4], 3))  # 2

# Binary search
def binary_search(arr, x):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == x: return mid
        elif arr[mid] < x: lo = mid+1
        else: hi = mid-1
    return -1
print(binary_search([1,2,3,4,5], 4))  # 3
