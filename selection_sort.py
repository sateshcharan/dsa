def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min_idx = i
        for j in range(i+1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr


if __name__ == '__main__':
    arr = [1,3,2,64,3,7,90,43,63]
    print(selection_sort(arr))