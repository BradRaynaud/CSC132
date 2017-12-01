dice_sums = [0] * 11

print "Die1\tDie2\tSum\t"
for die1 in range(1,7):
    for die2 in range(1,7):
        dice_sum = die1 + die2
        dice_sums[dice_sum-2]+= 1
        print"{}\t{}\t{}".format(die1,die2,dice_sum)

print"\tSum\tFreq\tProb"
for i in range(len(dice_sums)):
    print"{}\t{}\t{}".format(i+2,dice_sums[i],dice_sums[i]*1.0/sum(dice_sums))

