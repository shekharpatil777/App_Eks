# Quick Sort
def quicksort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right= [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))
# [1, 1, 2, 3, 6, 8, 10]

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right= merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i]); i+=1
        else:
            res.append(right[j]); j+=1
    res.extend(left[i:]); res.extend(right[j:])
    return res

print(merge_sort([5,2,4,6,1,3]))
# [1, 2, 3, 4, 5, 6]

