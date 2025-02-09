def swap(a, b, arr):
    arr[a], arr[b] =  arr[b], arr[a]

def partition (elements, p_index, end):
    pivot = elements[end]
    for i in range(p_index, end):
        if elements[i] <= pivot:
            swap(i, p_index, elements)
            p_index += 1
    swap(p_index, end, elements)
    return p_index


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

    tests = [
        [11,9,29,7,2,15,28,21,22,34,50],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')