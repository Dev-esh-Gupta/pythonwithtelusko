def binary_search(arr, search_ele):
    i, j = 0, len(arr) - 1

    while i <= j:
        m = (i + j) // 2

        if arr[m] == search_ele:
            return True
        elif arr[m] > search_ele:
            j = m - 1
        else:
            i = m + 1
    return False


arr = [2, 3, 4, 12, 23, 25, 66, 76, 89]

if binary_search(arr, 76):
    print('Found')
else:
    print('Not Found')
