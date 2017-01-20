def hanoi(n,src,dst,spr):
    if n == 1:
        print "{} -> {}".format(src, dst)
    else:
        hanoi(n-1,src,spr,dst)
        hanoi(1,src,dst,spr)
        hanoi(n-1,spr,dst,src)


hanoi(40,"A","C","B")