def binary_search(num_list, num_to_find):
    left_index = 0
    right_index = len(num_list)
    while left_index < right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = num_list[mid_index]
        if mid_number == num_to_find:
            return mid_index
        if mid_number < num_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1

def binary_search_recursion(num_list, num_to_find, left_index, right_index):
    mid_index = (left_index + right_index) // 2
    mid_number = num_list[mid_index]
    if mid_number == num_to_find:
        return mid_index
    if mid_number < num_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    if left_index > right_index:
        return -1
    return binary_search_recursion(num_list, num_to_find, left_index, right_index)

def find_occurance(num_list, num_to_find):
    index = binary_search(num_list, num_to_find)
    occurance = []
    occurance.append(index)

    #check occurance on left side
    i = 0
    while i < index:
        if num_list[i] == num_to_find:
            occurance.append(i)
        i += 1

    #check occurance on right side
    i = index + 1
    while i < len(num_list):
        if num_list[i] == num_to_find:
            occurance.append(i)
        i += 1

    return sorted(occurance)


if __name__ == '__main__':
    num_list = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    num_to_find = 15
    print(binary_search(num_list, num_to_find))
    print(binary_search_recursion(num_list, num_to_find, 0, len(num_list) - 1))
    print(find_occurance(num_list, num_to_find))
    