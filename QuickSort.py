import random


def randomizedPartition(arr, low, high):
    # randomize pivot
    pivot = random.randint(low, high)
    # swap pivot with last element
    x = arr[pivot]
    arr[pivot], arr[high] = arr[high], arr[pivot]
    # partition
    i = low - 1
    # loop through array
    for j in range(low, high):
        # if current element is smaller than pivot, swap with element after import
        if arr[j] <= x:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    # swap pivot with element after i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pivot = randomizedPartition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)


def findKthElement(arr, low, high, k):
    pivot = randomizedPartition(arr, low, high)
    if pivot == k - 1:
        return arr[pivot]
    elif pivot < k - 1:
        return findKthElement(arr, pivot + 1, high, k)
    else:
        return findKthElement(arr, low, pivot - 1, k)
