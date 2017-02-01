
def hanoi(n,src,dst,spr):
    counter = 0
    if n == 1:
        counter += 1
    else:
        hanoi(n-1,src,spr,dst)
        hanoi(1,src,dst,spr)
        hanoi(n-1,spr,dst,src)
    return counter

print hanoi(25,"A","C","B")

