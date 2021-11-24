class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

"""
s = Stack()
print(s.is_empty()) # True
s.push(4) # [4]
s.push('dog') # [4, 'dog']
print(s.peek()) # dog
s.push(True) # [4, 'dog', True]
print(s.size()) # 3
print(s.pop()) # True
print(s.size()) # 2
"""




