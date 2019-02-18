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


print(insertion_sort([5, 3, 2, 2, 4, 6, 9]))


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
