class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

d = Deque()

print(d.isEmpty())
print(d.addRear(4))
print(d.addRear('dog'))
print(d.addFront('cat'))
print(d.addFront(True))	 
print(d.size())
print(d.isEmpty())	
print(d.addRear(8.4)) 
print(d.removeRear())
print(d.removeFront())