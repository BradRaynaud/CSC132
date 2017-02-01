###########################################################################################
# Name: Brad Raynaud
# Date: 1/31/2017
# Description: This program solves question 3 & 4 of project euler
###########################################################################################
import math
# This function solves project euler problem 3 by finding the factors of the check number which is square root of the
# number 600,851,475,143. It does this via a for loop that checks to see if the number i is divisible by the original.
# If the number i is divisible then program calls the function Prime_Check to check if the number is prime. If prime the
# variable Hfactor("highest factor") is set equal to i
def problem3():
    num = 3 # sets num to 3 due to issues with prime check and the number 2
    n = 0 # initializes n
    assignment = 600851475143 # number that we are finding factors for
    check = int(math.sqrt(assignment))+1 # finds the square root of the assignment and converts it into an integer
    Hfactor = 0 # Initializes Hfactor
    # The function prime_check checks to see if the number x is prime. It does this by checking if the number x is
    # divisible by n. If the number is ever divisible by any number "1" is returned causing the loop to terminate
    def prime_check(x):
        n = 2 # initializes n
        while n != x - 1: # while n does not equal x - 1
            if x % n == 0: # checks to see if x is divisible by n
                return(1) # returns 1 if number is not prime
            n += 1 # increments n
        return(0) # returns 0 if number is prime

    for i in range(2,check): # for loop that goes from 2 to check-1
        if assignment % i == 0: # checks for factors
            if prime_check(i) == 0: # calls prime_check with the argument i
                Hfactor = i # sets new prime factor to Hfactor
    return Hfactor # returns final solution

# This function solves project euler problem 4 by finding the highest palindrome made up of two three digit numbers. It
# does this by checking for every possible multiplication of two 3 digit numbers. After generating a number the function
#  calls the function is_palindrome to check if the number is indeed a palindrome. If the function is_palindrome returns
# true then the number n is added to the list. following the completion of the for loop the function checks for the
# highest value in the list.
def problem4():
    list = [] # initializes list
# the function is_palindrome checks if the number x is a palindrome by comparing the string x to the string x reversed.
# If both strings are equivalent then the true is returns as the number is a palindrome.
    def is_palindrome(x):
        if str(x) == str(x)[::-1]: # compares the string x to the string x reversed
            return (True) # returns true if number is palindrome

    for x in range(100, 1000): # for loop that checks x in range 100 to 999
        for y in range(100, 1000): # for loop that checks y in range 100 to 999
            n = x * y # calculates the next number to plug into is_palindrome
            if is_palindrome(n) == True: # calls is_palindrome to check if the number is a palindrome
                list.append(n) # adds n to end of list if n is a palindrome

    return max(list) # returns the highest value in the list

print "The largest prime factor of the number 600,851,475,143 is {}".format(problem3())
print "The largest palindrome made from the products of two 3-digit numbers is {}".format(problem4())