from Node import Node

class UnorderedList:
    def __init__(self):
        self.head = None
    def add(self, item):
            newNode = Node(item)
            newNode.setNext(self.head)
            self.head = newNode
    def isEmpty(self):
        return self.head == None
    def size(self):
        count = 0
        current = self.head
        while(current != None):
            current = current.getNext()
            count += 1
        return count
    def search(self, item):
        current = self.head
        while (current != None):
            if current.getData() == item:
                return True
            current = current.getNext()
        return False
    def remove(self, item):
        previous = None
        current = self.head
        while current != None and current.getData() != item:
            previous = current
            current = current.getNext()
        if previous == None: # item was the head
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    


mylist = UnorderedList()
print(mylist.isEmpty())
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print(mylist.size())
print(mylist.search(17))