def binarySearch(list, item):
    first = 0
    last = len(list) - 1
    while(first <= last):
        middle = (first+last) // 2
        if list[middle] == item:
            return True
        elif list[middle] > item:
            last = middle - 1
        else:
            first = middle + 1
    return False

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))