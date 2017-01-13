# Project Euler Problem 3
# By Brad Raynaud

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
import math

# Python program to check if the input number is prime or not
num = 1
n = 0
assignment = 600851475143
check = int(math.sqrt(assignment))
Hfactor = 0

def prime_check(x):
    n = 2
    while n != x - 1:
        if x % n == 0:
            return(1)
        n += 1
    return(0)


while num != check:
    if check % num == 0 and prime_check(num) == 0:
        Hfactor = num
        print Hfactor
    num += 1

