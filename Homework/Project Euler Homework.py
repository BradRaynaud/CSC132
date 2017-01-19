




def problem1():
    num = 0
    total = 0
    while num < 1000:
        if num % 3 == 0:
            total += num
        if num % 5 == 0:
            total += num
        if num % 15 == 0:
            total -= num
        num += 1
    return total

print "The sum of all multiples 3 and 5 below 1000 are{}".format(problem1())