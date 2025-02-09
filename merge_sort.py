def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    rigth = merge_sort(right)
    return merge_two_arr(left, right)

def merge_two_arr(a, b):
    i = j = 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i+=1
        else:
            merged.append(b[j])
            j+=1
    while i < len(a):
        merged.append(a[i])
        i += 1
    while j < len(b):
        merged.append(b[j])
        j += 1
    return merged

if __name__ == '__main__':
    arr = [1,3,2,64,3,7,90,43,63]
    print(merge_sort(arr))