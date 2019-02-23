from collections import defaultdict

# Complete the selection_sort() function below in class with your instructor


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # find the smallest index after i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    if not arr:
        return arr
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i = j
            j = i - 1
    return arr




# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):
    result = arr[:]

    for i in range(len(result) - 1):
        for j in range(0, len(result) - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


# STRETCH: implement the Count Sort function below
# Why use count sort?
# Count sort is predictible in its sorting time. It requires two non-nested loops over n,
# and one loop over the range in values to be sorted. This means it can be reasonably
# efficient for sorting numbers that are very close together. But large ranges in numbers
# will make it impractible. Apparently it is useful when combined with radix sort for this reason
# as radix tends to cluster numbers within ranges.

# It also doesn't benefit from mostly sorted lists, as it will need to go through the same number of steps
# regardless. Some other sorting algorithms can take advantage of this, like insertion sort.


def count_sort(arr, maximum=-1):
    max = maximum if maximum >= 0 else 0
    count = defaultdict(int)
    # build up dictionary of occurences
    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        count[num] += 1
        if num > max:
            max = num
    # convert values into placement positons
    for i in range(1, max + 1):
        count[i] = count[i - 1] + count[i]
    # initialize result array
    output = [None] * len(arr)
    # loop over original array, and use count to determine position
    # lower count position by 1 after each addition to keep it current
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        pos = count[num] - 1
        output[pos] = num
        count[num] -= 1
    return output


def dict_count_sort(arr, k):
    count = defaultdict(int)
    # build up dictionary of occurences
    for num, val in arr:
        count[num] += 1
    # convert values into placement positions
    for i in range(1, k + 1):
        count[i] = count[i - 1] + count[i]
    # initialize result array
    output = [None] * len(arr)
    # loop over original array, and use count to determine position
    # lower count position by 1 after each addition to keep it current
    for i in range(len(arr) - 1, -1, -1):
        num, val = arr[i]
        pos = count[num] - 1
        output[pos] = val
        count[num] -= 1
    return output


def radix_sort(arr):
    lengths = defaultdict(list)
    for i in arr:
        str_val = str(i)
        lengths[len(str_val)].append(str_val)

    for length, equal_length_nums in lengths.items():
        for radix in range(length - 1, -1, -1):
            lengths[length] = dict_count_sort(
                [(int(number[radix]), number) for number in equal_length_nums], 9)

    result = []
    i = 1
    while lengths:
        equal_length_nums = lengths[i]
        if equal_length_nums:
            result.extend(equal_length_nums)
            del lengths[i]
        i += 1
    return result
