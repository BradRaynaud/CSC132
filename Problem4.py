




list = []

def is_palindrome(x):
    if str(x) == str(x)[::-1]:
        return(True)

for x in range(100,999):
    for y in range(100,999):
        n = x*y
        if is_palindrome(n) == True:
            list.append(n)

print max(list)

