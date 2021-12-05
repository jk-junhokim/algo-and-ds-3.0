def sequential_search_practice(a_list, item):

    pos = 0
    found = False

    while (pos < len(a_list)) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    return found

# test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(sequential_search_practice(test_list, 13))
# print(sequential_search_practice(test_list, 3))

def binary_search_practice(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        pos = len(a_list) // 2

    if a_list[pos] == item:
        return True
    else:
        if a_list[pos] < item:
            return binary_search_practice(a_list[pos + 1:], item)
        else:
            return binary_search_practice(a_list[:pos], item)


# test_list = [1, 2, 3, 8, 17, 19, 24, 155, 200]
# print(binary_search_practice(test_list, 2))
# print(binary_search_practice(test_list, 88))

def bubble_sort_practice(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
    

a_list = [1, 5, 2, 60, 22, 31, 41, 17]
bubble_sort_practice(a_list)
print(a_list)

def short_bubble_sort_practice(a_list):
    pass