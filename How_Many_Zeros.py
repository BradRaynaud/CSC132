n = 1
count = 0
zeros = 0
iteration = 0

while n != 1000000:
    zeros += str(n).count("0")
    n += 1

print zeros