def shell_sort(arr):
    size = len(arr)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            j = i
            while j > gap and arr[j-1] > arr[j]:
                arr[j], arr[j - 1] = arr[j -1], arr[j]
                j -= 1
        gap = gap // 2
    return arr

if __name__ == '__main__':
    arr = [1,3,2,64,3,7,90,43,63]
    print(shell_sort(arr))