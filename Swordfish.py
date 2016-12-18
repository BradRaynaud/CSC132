# Simple Password program
# By Brad Raynaud

n = 0
password = ""
correct_pass = "Swordfish"
while n != 1:
    print("Who are you?")
    name = input()
    if name == "Brad":
        while password != correct_pass:
            print("What is the password Brad?")
            password = input()
            if password != correct_pass:
                print("incorrect")
            else:
                print("Access Granted")
        break
    else:
        print"Hello, it is nice to meet you {}".format(name)
