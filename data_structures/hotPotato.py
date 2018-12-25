from queue  import Queue

def hotPotato(array, number):
    q = Queue()
    for name in array:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(number):
            temp = q.dequeue()
            
            q.enqueue(temp)
        q.dequeue()
        
    return q.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))