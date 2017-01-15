# Generates a large amount of random numbers and gathers data
import random
n = input()
rand = []
while n != 0:
    rand.append(random.randint(1,100))
    n -= 1
rand.sort()
print rand
print "The list has {} Items".format(len(rand))
print min(rand)
print max(rand)


