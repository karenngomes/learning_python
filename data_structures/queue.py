class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        return self.items.append(item) # Big-O: O(1)
    def dequeue(self):
        return self.items.pop(0) # Big-O: O(n)
    def size(self):
        return len(self.items)
"""
q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
q.dequeue()
print(q.items)
"""