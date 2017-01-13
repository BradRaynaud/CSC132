n = 1
count = 0

def drew(x):
    zeros = 0
    while x != 0:
        if x % 10 == 0:
            zeros += 1
        x = x/10
    return(zeros)

while n <= 1000000:
    count = count + drew(n)
    n = n + 1

print count