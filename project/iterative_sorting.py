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
    result = [arr[0]]
    for i in range(1, len(arr)):
        tmp = arr[i]
        result.append(tmp)
        for j in range(len(result) - 1, 0, -1):
            if result[j] < result[j - 1]:
                result[j], result[j - 1] = result[j - 1], result[j]
            else:
                break
    return result


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):
    result = arr[:]

    for i in range(len(result) - 1):
        for j in range(0, len(result) - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


# STRETCH: implement the Count Sort function below


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
