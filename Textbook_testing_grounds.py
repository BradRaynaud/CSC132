def foo(n):
    if n == 1:
        return 1
    else:
        x = foo(n-1)
        x = x + 3*n -2
        return x

print foo(2)

x = 0
terms = []
for i in range(1,8):
    if i == 1:
        x += 1
        terms.append(x)
    else:
        x = x+3*i-2
        terms.append(x)

print terms
print int("0xFF0000",0)
print int("0x00FF00",0)
print int("0x0000FF",0)
print hex(255)