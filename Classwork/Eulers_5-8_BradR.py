###########################################################################################
# Name: Brad Raynaud
# Date: 2/10/2017
# Description: This program solves problems 5,6, 7, and 8 of project euler
###########################################################################################
from math import floor, sqrt

# This function checks if a number is divisible by all the numbers from 1-20 by checking if the number is divisible
# by 9,19. It only goes from 9,19 because all other numbers below that are factors of some number between 9 to 19
def div_check(x):
    for n in range(19, 10, -1): # starts with 19 first and ends with 9
        if x % n == 0:  # checks to see if number is divisible by n
            continue
        else:  # If number is ever not divisible by n the function returns False
            return (False)
    return (True) # returns True at end of for loop

# this function returns True if the number x is prime. It does this first by checking if the number x is divisible by 2
# then flooring the square root of the number x. Then it checks every number from 3 to sqrtn to see if the number is
# prime. If x is ever divisible by any number other than 1 and itself the function returns false
def prime_check(x):
    if x % 2 == 0:  # checks to see if x is divisible by 2
        return False  # if yes return false
    sqrtn = floor(sqrt(x)) + 1  # floors the square root of xw
    sqrtn = int(sqrtn)  # ensures that sqrtn is an integer
    for n in range(3, sqrtn, 1):  # for loop for 3 to sqrtn
        if x % n == 0:  # if x is ever divisible by any number returns false
            return False
    return True  # returns true if number is prime

# This function solves problem 5 by calling div check to see if the number num is divisible by all numbers 1-20
# while not true the function increments by 2520 which happens to be a number that is divisible by all numbers 1-10
def problem5():
    num = 2520  # initializes num
    while div_check(num) != True:  # While div check does not return true
        num += 2520  # increments num by 2520
    return num  # returns num when solution is found

# This function find the difference between the sum of squares and the square of sum of the first 100 natural numbers.
# it does this by incrementing x and y by the sum of squares and the square of sum respectively. Then the function finds
# the answer by subtracting x from y
def problem6():
    answer = 0  # initializes answer
    x = 0  # initializes x
    y = 0  # initializes y
    for i in range(1, 101):  # goes from 1-100
        x += i ** 2  # increments x by the sum of the sqares
    for j in range(1, 101):  # goes from 1-100
        y += j # increments y by j from 1-100
    y = y ** 2  # squares y
    answer = y - x  # finds answer
    return answer  # returns solution

# this function finds the 10,001st prime by calling the prime_check function to find if the number n is prime. If prime
# the number x is incremented to show that a prime number has been found
def problem7():
    x = 0  # initializes x
    n = 1  # initializes x at 1 to avoid issues with primes below 10
    while x != 10000:  # while 10,001 prime is not found
        n += 2 # Increments x by two because a prime can never be even
        if prime_check(n) == True:  # calls prime_check function and if it returns true prime is found
            x += 1  # increments x by 1 to show that a prime was found
    return n  # returns solution

# this function finds the greatest product of thirteen adjacent digits. The function does this by multiplying all
# occurrences of 13 adjacent digits.
# SideNote: I was unable to store the number a in any other way.
def problem8():
    # initialises the numbers in integer form
    a = (7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
    b = str(a)  # converts a into string b
    c = []  # initializes list
    n = 0  # initializes current list position
    total = 0  # initializes the answer variable
    # converts the string b into the list c
    for digit in b:
        c.append(int(digit))  # appends the list c with every character in string b

    while n != 986:  # while n does not equal 986(1000-13-1)
        # finds the product of the thirteen adjacent digits
        localmax = c[n] * c[n + 1] * c[n + 2] * c[n + 3] * c[n + 4] * c[n + 5] * c[n + 6] * c[n + 7] * c[n + 8] * c[
            n + 9] * c[n + 10] * c[n + 11] * c[n + 12]
        if localmax > total:  # if current product is higher than total
            total = localmax  # set total to new maximum
        n += 1  # increments n
    return total  # returns solution

# the main part of the program
print "The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {}".format(problem5())

print "The difference between the sum of squares and square of sum of the first 100 natural numbers is {}".format(problem6())

print "The 10,001st prime number is {}".format(problem7())

print "The greatest product of thirteen adjacent digits is {}".format(problem8())
