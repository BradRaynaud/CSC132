# Searching and sorting
# Brad Raynaud
import math
list = [5, 13, 4, 9, 7, 11, 2, 8, 12]
#list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
first = 0
last = len(list) - 1

list.sort()
print list
print"What are you looking for?"
num = input()

while first <= last:
    mid = int(math.floor((first+last)/2))
    if num == list[mid]:
        print"{} has been found".format(num)
        exit()
    elif num > list[mid]:
        first = mid + 1
    else:
        last = mid - 1
print"{} has not been found".format(num)