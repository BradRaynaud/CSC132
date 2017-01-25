######################################################################
# Name: Brad Raynaud
# Date: 1/23/2017
# Description: This program finds the sum of two 7 bit binary numbers
######################################################################
import Rpi.GPIO as GPIO #imports GPIO functionality
from random import randint #imports randint for number generation

def setGPIO():
    gpio = [4,17,27,22,5,6,13,19,26]
    for i in gpio:
        GPIO.setup(i, GPIO.out)
    return gpio

def setNum():
    num = []
    for i in range(0,8):
        num.append(randint(0,1))
    return num

def display():
    for i in range(len(sum)):
        if sum[i] == 1:
            GPIO.output(gpio[i], GPIO.HIGH)
        else:
            GPIO.output(gpio[i], GPIO.LOW)

def fulladder(Cin, A, B):
    S = 0
    Cout = 0
    s1 = A ^ B
    c = A & B
    S = s1 ^ Cin
    c1 = s1 & Cin
    Cout = c1 | c
    return S, Cout

def calculate(num1,num2):
    Cout = 0
    sum = []
    n = len(num1) - 1

    while n >= 0:
        A = num1[n]
        B = num2[n]
        Cin = Cout
        S, Cout = fulladder(Cin, A, B)

        sum.insert(0, S)
    sum.insert(0,Cout)
    return sum

    GPIO.setmode(GPIO.BCM)
    gpio = setGPIO()
    num1 = setNum()
    print "      ", num1
    num2 = setNum()
    print "      ", num2
    sum = calculate(num1, num2)
    print "= ", sum
    display()
    raw_input("Press ENTER to terminate")
    GPIO.cleanup()

