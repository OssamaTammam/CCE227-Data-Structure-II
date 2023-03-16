def selectionSort(arr):
    # loop through array
    for i in range(len(arr) - 1):
        min = i;
        # loop through elements after current element to find the smallest element
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        # swap the smallest element with current element into correct position
        arr[min], arr[i] = arr[i], arr[min]
