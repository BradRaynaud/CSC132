num = 20

def div_check(x):
    for n in range(1,20):
       if x % n == 0:
           continue
       else:
            return(False)
    return(True)

while div_check(num) != True:
    num += 20

print num



