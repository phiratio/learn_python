import math


def merge_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    length = len(arr)
    middle = math.floor(length / 2)
    left = arr[0:middle]
    right = arr[middle:]

    return merge(merge_sort(left), merge_sort(right))


# left and right will always be ordered!
def merge(left: list, right: list) -> list:
    results = []
    while len(left) and len(right):
        if left[0] <= right[0]:
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))
    # left or right is empty arr at this moment
    return results + left + right


merge_sort_test_arr = [7, 8, 4, 5, 7, 8, 9, 1, 2, 3, 7, 8]
print(merge_sort(merge_sort_test_arr))
print(merge_sort([1]))
print(merge_sort([2, 1]))
print(merge_sort([2, 1, 3]))

# find median element from 2 sorted lists
arr1 = [4, 6, 7, 3]
arr2 = [2, 8, 9]


def median_finder(array_1: list, array_2: list):
    array_1 = merge_sort(array_1)
    array_2 = merge_sort(array_2)
    counter = math.ceil(
        len(array_1 + array_2) / 2.0
    )
    results = []
    while counter > 0:
        counter -= 1
        if array_1[0] <= array_2[0]:
            results.append(array_1.pop(0))
        else:
            results.append(array_2.pop(0))
    return results[-1]


print(median_finder(arr1, arr2))
