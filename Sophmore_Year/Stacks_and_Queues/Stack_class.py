# Stack class in python
# 11/30/2017
# Brad Raynaud

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    # you can use the native pop command because the newest item in the stack is the last item in the list
    # and the pop command without an argument removes the last item from the list
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
