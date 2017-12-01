import math
def question3():
    num = 3
    n = 0
    assignment = 600851475143
    check = int(math.sqrt(assignment)) + 1
    Hfactor = 0
    def prime_check(x):
        n = 2
        while n != x - 1:
            if x % n == 0:
                return (1)
            n += 1
        return (0)
    while num < check:
        if num % 2 == 1:
            if prime_check(num) == 0:
                if assignment % num == 0:
                    Hfactor = num
        num += 1

    return Hfactor

def question4():
    list = []

    def is_palindrome(x):
        if str(x) == str(x)[::-1]:
            return (True)

    for x in range(100, 999):
        for y in range(100, 999):
            n = x * y
            if is_palindrome(n) == True:
                list.append(n)

    return max(list)

print question3()
print question4()