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

def binary_search_practice(a_list):

    found = False


    return found


test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(binary_search_practice(test_list, 13))
print(binary_search_practice(test_list, 3))

def bubble_sort_practice(a_list):
    pass

def short_bubble_sort_practice(a_list):
    pass