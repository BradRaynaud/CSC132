# printing little jimmy and Incrementing
# By:Brad Raynaud

def end():
    exit()

jimmy_count = 0
print("How many?")
n = input()
print("My name is")
while n != 0:
    print("Jimmy Five Times ({})").format(jimmy_count)
    n = n - 1
    jimmy_count = jimmy_count + 1
#Testing pull command
#hello from Microsoft Surface