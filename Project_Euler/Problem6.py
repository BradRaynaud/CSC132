def sum_sq(n):
    return sum([i for i in range(n+1)])**2-sum([i**2 for i in range(n+1)])

print sum_sq(100)
