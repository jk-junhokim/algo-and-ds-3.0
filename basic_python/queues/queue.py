class Queue:
    def __init__(self):
        self.items = []

    def push(self, object):
        self.items.append(object)

    def pop(self):
        self.items.pop(0)