# STRETCH: implement Linear Search
def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1

    low = 0
    high = len(arr)-1
    # edge case where final index is missed, due to rounding down index
    if arr[high] == target:
        return high

    while low < high:
        middle = (high + low) // 2
        if arr[middle] == target:
            return middle

        elif arr[middle] > target:
            high = middle
        else:
            low = middle

    return -1  # not found


# print(binary_search([1, 3, 4, 5, 8, 11, 12, 13], 4))
# print(binary_search([1, 3, 4, 5, 8, 11, 12, 13], 11))
# print(binary_search([1, 3, 4, 5, 8, 11, 12, 13], 1))
# print(binary_search([1, 3, 4, 5, 8, 11, 12, 13], 13))

# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low=None, high=None):
    low = 0 if low is None or low < 0 else low
    high = len(arr) - 1 if high is None or high < 0 else high

    middle = (low+high) // 2

    if len(arr) == 0:
        return -1  # array empty

    middle_val = arr[middle]
    if middle_val == target:
        return middle
    elif middle_val > target:
        return binary_search_recursive(arr, target, low, middle)
    elif arr[high] == target:
        return high
    else:
        return binary_search_recursive(arr, target, middle, high)


print(binary_search_recursive([1, 3, 4, 5, 8, 11, 12, 13], 4))
print(binary_search_recursive([1, 3, 4, 5, 8, 11, 12, 13], 11))
print(binary_search_recursive([1, 3, 4, 5, 8, 11, 12, 13], 1))
print(binary_search_recursive([1, 3, 4, 5, 8, 11, 12, 13], 13))
