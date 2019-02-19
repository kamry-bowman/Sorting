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
        pivot = (low + high) // 2
        lo = low
        hi = high
        # iterate over indexes to the left of pivot
        while lo < pivot:
            # continue through index as long as values are less than pivot value
            if arr[lo] <= arr[pivot]:
                lo += 1
            # if left value is greater than pivot value, start decrementing right pointer
            # looking for a matching inversion on the right side
            if arr[lo] > arr[pivot]:
                right_match = False
                while hi > pivot and not right_match:
                    if arr[hi] <= arr[pivot]:
                        right_match = True
                    else:
                        hi -= 1
                # if a matching inversion on right is found, then swap
                if right_match:
                    arr[lo], arr[hi] = arr[hi], arr[lo]
                    lo += 1
                    hi -= 1
                # otherwise, swap to immediate left of pivot, and then swap with pivot
                else:
                    arr[lo], arr[pivot - 1] == arr[pivot - 1], arr[lo]
                    arr[pivot - 1], arr[pivot] = arr[pivot], arr[pivot - 1]
                    pivot -= 1
        # iterate over indexes to the right of pivot, perform symmetric logic
        while hi > pivot:
            if arr[hi] >= arr[pivot]:
                hi -= 1
            if arr[hi] < arr[pivot]:
                arr[hi], arr[pivot + 1] = arr[pivot + 1], arr[hi]
                arr[pivot], arr[pivot + 1] = arr[pivot + 1], arr[pivot]
                pivot += 1

        # recur on left
        print(low, pivot - 1)
        quick_sort(arr, low, pivot - 1)

        # recur on right
        quick_sort(arr, pivot + 1, high)

        return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
