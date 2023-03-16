import random


def randomizedPartition(arr, p, r):
    pivot = random.randint(p, r)
    x = arr[pivot]
    arr[pivot], arr[r] = arr[r], arr[pivot]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quickSort(arr, p, r):
    if p < r:
        q = randomizedPartition(arr, p, r)
        quickSort(arr, p, q - 1)
        quickSort(arr, q + 1, r)
