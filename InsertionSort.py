def insertionSort(arr):
    # loop through array
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        # loop through elements before current element to find correct position
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arr[i]
