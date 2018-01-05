# Project Euler Question 2
# By Brad Raynaud
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

x1 = 1
x2 = 0
current = 0
total = 0
while current < 4000000:
    current = x1 + x2
    if current % 2 == 0:
        total += current
    x1 = x2
    x2 = current

print total