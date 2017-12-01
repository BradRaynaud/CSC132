# Queue class in python
# 11/30/2017
# Brad Raynaud

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def enQueue(self,item):
        self.items.append(item)

    def deQueue(self):
        return self.items.pop(0)



