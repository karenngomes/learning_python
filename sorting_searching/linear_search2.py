# ordered list
def linearSearch2(list, item):
    i = 0
    while(i < len(list)):
        if list[i] == item:
            return True
        elif list[i] > item:
            return False
        i += 1
    return False

print(linearSearch2([1,2,3,4,5,7,8,20], 3))
print(linearSearch2([1,2,3,4,5,7,8,20], 23))