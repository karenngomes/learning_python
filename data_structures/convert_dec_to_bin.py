from stack import Stack

def converterToBin(number):
    s = Stack()
    while number > 0:
        s.push(number % 2)
        number = number // 2
    binary = ''
    for i in range(s.size()):
        binary += str(s.pop())
    return binary
n = int(input())
print(converterToBin(n))