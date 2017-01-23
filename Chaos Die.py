from random import randint, seed

def roll():
    return randint(1,6)

print "How many rolls of two dice would you like to simulate?"
num_rolls = input()
print"What pseudo random number generator seed would you like to use"
rand_seed = input()
dice_sums = [0] * 11

print"Rolling two dice {} times with a seed of {}.".format(num_rolls,rand_seed)

seed(rand_seed)
print"Die 1\tDie 2\tSum"
for i in range(0, num_rolls):
    die1 = roll()
    die2 = roll()
    dice_sums = die1 + die2
    dice_sums[dice_sums-2] += 1
    print "{}\t{}\t{}".format(die1,die2,dice_sums)

print "\nSum\tFreq\tProb"
for i in range(len(dice_sums)):
    print"{}\t{}\t{}".format(i+2,dice_sums[i],dice_sums[i]* 1.0 / sum(dice_sums))