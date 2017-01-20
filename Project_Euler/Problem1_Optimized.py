num = 0
total = 0
while num < 1000:
    if num % 3 == 0:
        total += num
    if num % 5 == 0:
        total += num
    if num % 15 == 0:
        total -= num
    num += 1
