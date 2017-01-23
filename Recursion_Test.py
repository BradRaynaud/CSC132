print"What Factorial would you like to calculate"
x = input()

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print"5! = {}".format(fact(x))