def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]


arr = [2, 3, 12, 3, 5, 6, 7, 12, 5, 11]
bubble_sort(arr)
print(arr)

