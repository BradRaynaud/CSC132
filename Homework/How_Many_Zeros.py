###########################################################################################
# Name: Brad Raynaud
# Date: January 12, 2017
# Description: This program calculates the number of zeros written from one to one million.
###########################################################################################
n = 1
zeros = 0 # Initializes the zero counter

while n <= 1000000:
    num = n #sets num
    num = str(num)  # Sets converts num to a string
    zeros += num.count("0") # Counts the zeros in num
    n += 1      # Increment n
    
print zeros     # Print Result