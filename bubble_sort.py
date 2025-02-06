def bubble_sort(num_list):
    swapped = false
    i = 0
    for i in range(len(num_list) - 1):
        for j in range(len(num_list)-1-i):
            if num_list[j] > num_list[j + 1]:
                temp = num_list[j]
                num_list[j] = num_list[j + 1]
                num_list[j + 1] = temp
                swapped = true
        if swapped == false:
            break
    return num_list

numbers = [1,3,5,5,4,2,9,8]
print(bubble_sort(numbers))