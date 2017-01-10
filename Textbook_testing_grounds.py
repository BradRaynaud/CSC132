a = 10

def f(x):
    a = 11
    b = 21
    x *= 2
    print "in F(): a={}, b={}, x={}".format(a,b,x)


b = 20
f(b)
print "in main: a={},b={} x={}".format(a,b,x)


def g():
    global a
    a *= 1.5
    print "in g(): a={}, b={}".format(a,b)

g()
print "in main: a={}, b={}".format(a,b)
