from deque import Deque

def palindChecker(string):
    d = Deque()
    for i in range(len(string)):
        d.addRear(string[i])
    middle = len(string) // 2
    for i in range(middle):
        first = d.removeRear()
        last = d.removeFront()
        if(first != last):
            return False
    return True

print(palindChecker("radar"))