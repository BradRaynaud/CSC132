# Project Euler Question 1
# By: Brad Raynaud
#
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
num = 0
total = 0
num2 = 0
num3 = 0

while num < 1000:
    num += 5
    if num < 1000:
        total += num

while num2 < 1000:
    num2 += 3
    if num2 < 1000:
        total += num2

while num3 < 1000:
    num3 += 15
    if num3 < 1000:
        total -= num3
print total
