from basic_python.stacks.stack import Stack

def par_checker_simple(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()

        index += 1
    
    if balanced and s.is_empty():
        pass
    else:
        balanced = False

    return balanced

# print(par_checker_simple('((()))'))
# print(par_checker_simple('(()'))

def par_checker_general(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                opening_par = s.pop()
                closing_par = symbol
                if not is_symmetric(opening_par, closing_par):
                    balanced = False

        index += 1
    
    if balanced and s.is_empty():
        pass
    else:
        balanced = False

    return balanced

def is_symmetric(opening_par, closing_par):
    opens = "[{("
    closes = "]})"

    return opens.index(opening_par) == closes.index(closing_par)

print(par_checker_general('{{([][])}()}'))
print(par_checker_general('[{()]'))