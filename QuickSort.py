import random


def quickSort(arr, start, end):
    if end <= start:  # base case
        return
    else:
        pivot = partition(arr, start, end)
        quickSort(arr, start, pivot - 1)
        quickSort(arr, pivot + 1, end)


def partition(arr, start, end):
    pivot = random.randint(start, end)
    i = start - 1
    for j in range(start, end):
        if arr[j] < arr[pivot]:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    i += 1
    (arr[i], arr[pivot]) = (arr[pivot], arr[i])
    return i
