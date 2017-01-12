n = 1
zeros = 0

while n <= 1000000:
    num = n
    num = str(num)
    zeros += num.count("0")
    n += 1

print zeros