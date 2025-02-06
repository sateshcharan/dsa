
def binary_search(num_list, target):
    left_index = 0
    right_index = len(num_list) - 1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if num_list[mid_index] == target:
            return mid_index
        if num_list[mid_index] < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1

def binary_search_recursive(num_list, target, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = num_list[mid_index]

    if mid_number == target:
        return mid_index
    if mid_number < target:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(num_list, target, left_index, right_index)

    

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(num_list, 10))
print(binary_search_recursive(num_list, 10, 0, len(num_list) - 1))