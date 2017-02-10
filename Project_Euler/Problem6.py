def sum_sq(n):
    return sum([i for i in range(n+1)])**2-sum([i**2 for i in range(n+1)])

def problem6():
    answer = 0
    x = 0
    y = 0
    for i in range(1, 101):
        x += i ** 2
    for j in range(1, 101):
        y += j
    y = y ** 2
    answer = y - x
    return answer

print sum_sq(100)
print problem6()
