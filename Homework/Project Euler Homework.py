###########################################################################################
# Name: Brad Raynaud
# Date: 1/19/2017
# Description: This program solves questions 1 & 2 of Project Euler
###########################################################################################
def problem1():
    num = 0 # Initializes num
    total = 0 # Initializes num
    while num < 1000: # While Loop that stops when num < 1000
        if num % 3 == 0: # Looks for multiples of 3
            total += num # Adds multiple of 3 to total
        if num % 5 == 0: # Looks for multiples of 5
            total += num # Adds multiple of 5 to total
        if num % 15 == 0: # Looks for multiples of 15
            total -= num # Subtracts multiple of 15 from total
        num += 1 # Increments num
    return total # Returns answer
def problem2():
    x1 = 1 # Initializes storage variable 1
    x2 = 0 # Initializes storage variable 2
    current = 0 # Initializes current
    total = 0 # Initializes total
    while current < 4000000: # While loop that terminates when the Fibonacci current > 4 million
        current = x1 + x2 # Finds next fibonacci
        if current % 2 == 0: # Checks to see if current is even
            total += current # Adds current to total
        x1 = x2 # shifts x2 to x1 to find next Fibonacci value
        x2 = current # Stores Current
    return total # Returns Answer
print "The sum of all multiples of 3 or 5 below 1000 is {}".format(problem1())
print "The sum of all even-valued Fibonacci terms not exceeding four million is {}".format(problem2())
