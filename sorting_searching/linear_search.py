def linearSearch(list, item):
    i = 0
    while(i < len(list)):
        if list[i] == item:
            return True
        i += 1
    return False

print(linearSearch([1,8,20,2,3,15,4,5,7], 3))
print(linearSearch([1,8,20,2,3,15,4,5,7], 23))