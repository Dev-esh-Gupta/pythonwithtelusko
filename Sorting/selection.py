arr = [2, 3, 12, 3, 5, 6, 7, 12, 5, 11]


def selection_sort(arr):
    for i in range(len(arr)):
        mini = arr[i]
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < mini:
                mini = arr[j]
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)


selection_sort(arr)

print(arr)
