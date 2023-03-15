def mergeSort(arr):
    length = len(arr)
    if length <= 1:
        return
    middle = length // 2
    left = arr[:middle]
    right = arr[middle:]
    mergeSort(left)
    mergeSort(right)
    merge(arr, left, right)


def merge(arr, left, right):
    nleft = len(arr) // 2
    nright = len(arr) - nleft
    i = 0  # original arr
    l = 0  # left array
    r = 0  # right array

    # sorting the smaller arrays' elements into the original array
    while l < nleft and r < nright:
        if left[l] < right[r]:
            arr[i] = left[l]
            i += 1
            l += 1
        else:
            arr[i] = right[r]
            i += 1
            r += 1

    # checking if there is any elements left in the smaller arrays
    while l < nleft:
        arr[i] = left[l]
        i += 1
        l += 1
    while r < nright:
        arr[i] = right[r]
        i += 1
        r += 1
