def ACM(n):
    x= 50
    x += n
def BlueRoom(n):
    global x
    x *= n
x= 5
ACM(10)
BlueRoom(5)
x -= 1
print (x)