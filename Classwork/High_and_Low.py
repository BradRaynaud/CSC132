# using functions to find the high and low number

def high(a,b):
    if a>b:
        return a
    else:
        return b

def low(a,b):
    if a<b:
        return a
    else:
        return b

print("Please give me a number")
a = input()
print("Please give me another number")
b = input()

print("{} is the highest number").format(high(a,b))
print("{} is the lowest number").format(low(a,b))