from stack import Stack

def parChecker(string):
    size = len(string)
    valid = {'(',')'}
    if size == 0 or size % 2 != 0:
        return 'Não está balanceado!'
    elif set(string) != valid:
        return 'Não é possível balancear!'
    myStack = Stack()
    for i in range(size):
        if string[i] == '(':
            myStack.push(string[i])
        else:
            if(myStack.isEmpty()):
                return 'Não está balanceado!'
            myStack.pop()
    if(myStack.isEmpty()):
        return 'Está balanceado!'
    else:
        return 'Não está balanceado!'


str = input()
print(parChecker(str))
"""
x = Stack()
print(x.isEmpty())
x.push(3)
print(x)
"""