
def insertion_sort(elements):
    for i in range(1, len(elements)):
        j = i
        while j > 0 and elements[j-1] > elements[j]:
            elements[j], elements[j-1] = elements[j-1], elements[j]
            j -= 1

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    insertion_sort(elements)
    print(elements)

    # tests = [ 
    #     [11,9,29,7,2,15,28,21,22,34,50],
    #     [3, 7, 9, 11],
    #     [25, 22, 21, 10],
    #     [29, 15, 28],
    #     [],
    #     [6]
    # ]

    # for elements in tests:
    #     insertion_sort(elements)
    #     print(f'sorted array: {elements}')