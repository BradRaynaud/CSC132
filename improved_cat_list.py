# Improved Cat List

catnames = []
while True:
    print("enter the name of cat {} (Or Enter nothing to stop.)").format(len(catnames)+1)
    name = input()
    if name == "exit":
        break
    catnames = catnames + [name]
    print(name)
print ("The cat names are:")
for name in catnames:
    print(name)