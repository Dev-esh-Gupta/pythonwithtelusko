pos = -1

def search(arr, search_ele):
    for i in range(len(arr)):
        if arr[i] == search_ele:
            globals()['pos'] = i
            return True

    return False


arr = [5, 8, 6, 4, 1, 0, 12, 3]

search_ele = 1

if search(arr, search_ele):
    print("Found at position", pos)
else:
    print("Not Found")

