def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp
    
# a_list = [1, 5, 2, 60, 22, 31, 41, 17]
# bubble_sort(a_list)
# print(a_list)

def short_bubble_sort(a_list):
    exchanges = True 
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
        pass_num = pass_num - 1

# a_list = [1, 5, 2, 60, 22, 31, 41, 17]
# short_bubble_sort(a_list)
# print(a_list)