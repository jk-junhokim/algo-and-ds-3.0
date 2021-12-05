def insertion_sort(a_list):
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    
# a_list = [54, 29, 92, 15, 77, 6, 44, 10]
# insertion_sort(a_list)
# print(a_list)