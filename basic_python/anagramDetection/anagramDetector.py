# one string is an anagram of another if the second is simply a rearrangement of the first
# assume the length of the strings are equal

def anagram_solution_1(s1, s2):
    a_list = list(s2)

    index_1 = 0
    is_anagram = True

    while index_1 < len(s1) and is_anagram:
        index_2 = 0
        found  = False
        while index_2 < len(a_list) and not found:
            if s1[index_1] == a_list[index_2]:
                found = True
            else:
                index_2 = index_2 + 1
        
        if found:
            a_list[index_2] = None
        else:
            is_anagram = False

        index_1 = index_1 + 1

    return is_anagram

# print(anagram_solution1("abcd", "cbda"))
# print(anagram_solution1("apple", "apble"))

def anagram_solution_2(s1, s2):
    a_list = [] * 26
    a_list_index = 0

    list_form_1 = list(s1)

    for letter in list_form_1:
        if letter not in a_list:
            a_list[a_list_index] += 1
        else:
            proper_index = a_list.index(letter)
            a_list[proper_index] += 1

    return

print(anagram_solution_2("abcd", "cbda"))
print(anagram_solution_2("apple", "apble"))

def anagram_solution_3(s1, s2):

    return

    