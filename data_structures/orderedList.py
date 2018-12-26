from Node import Node

class OrderedList:
    def __init__(self):
        self.head = None
    def add(self, item): # O(n)
        previous = None
        current = self.head
        newNode = Node(item)
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            newNode.setNext(self.head)
            self.head = newNode
        else:
            newNode.setNext(current)
            previous.setNext(newNode)
    def isEmpty(self): # O(1)
        return self.head == None
    def size(self): # O(n)
        count = 0
        current = self.head
        while(current != None):
            current = current.getNext()
            count += 1
        return count
    def search(self, item): # O(n)
        current = self.head
        while (current != None):
            if current.getData() == item:
                return True
            elif current.getData() > item:
                return False
            current = current.getNext()
        return False
    def printList(self): # O(n)
        current = self.head
        while(current != None):
            print(current.getData())
            current = current.getNext()

mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.add(53)
mylist.add(42)
mylist.add(45)
mylist.add(22)
mylist.add(31)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
# print(mylist.printList())
        