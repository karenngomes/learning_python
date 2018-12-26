"""
def bubbleSort(list):
    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
"""
def bubbleSort(list):
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]

list = [54,26,93,17,77,31,44,55,20]
bubbleSort(list)
print(list)