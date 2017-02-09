num = 2520

def div_check(x):
    for n in range(19,10, -1):
       if x % n == 0:
           continue
       else:
            return(False)
    return(True)

while div_check(num) != True:
    num += 2520

print num
