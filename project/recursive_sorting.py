# helper function
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range(0, elements):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# recursive sorting function
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# quick_sort, pivot in middle to avoid disturbing mostly sorted lists
def quick_sort(arr, low, high):
    if low >= high:
        return arr
    else:
        pivot_val = arr[(low + high) // 2]
        lo = low
        hi = high
        partition = None

        # iterate over indexes to the left of pivot
        while partition is None:
            print(pivot_val, lo, hi, arr)
            while arr[lo] < pivot_val:
                lo += 1

            # or case handles infinite loops when left and right pointers have equal values
            while arr[hi] > pivot_val or (arr[hi] == arr[lo] and hi - 1 > lo):
                hi -= 1

            if lo < hi and not (arr[hi] == arr[lo]):
                arr[lo], arr[hi] = arr[hi], arr[lo]
            else:
                partition = lo

        # recur on left
        quick_sort(arr, low, partition - 1)

        # recur on right
        quick_sort(arr, partition + 1, high)

        return arr

arr = [4,2,1,88,32,43,23,0,89, 9, 10]
print(quick_sort([4,2,1,88,32,43,23,0,89, 9, 10], 0, len(arr) - 1))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
