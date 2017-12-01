x = 0
n = 1
def prime_check(x):
    n = 2
    while n != x - 1:
        if x % n == 0:
            return(1)
        n += 1
    return(0)


while x != 10000:
    n += 2
    if prime_check(n) == 0:
        x += 1

print n