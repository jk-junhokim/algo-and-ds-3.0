class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.itmes == []

    def push(self, object):
        self.items.append(object)

    def pop(self):
        self.items.pop(0)