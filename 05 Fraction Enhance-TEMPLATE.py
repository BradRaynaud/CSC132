######################################################################################################################
# Name: 
# Date: 
# Description: 
######################################################################################################################

class Fraction(object):
	# write your code for the fraction class here



# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
# create some fractions
f1 = Fraction()
f2 = Fraction(5, 8)
f3 = Fraction(3, 4)
f4 = Fraction(1, 0)

# display them
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4

# play around
f3.num = 5
f3.den = 8
f1 = f2 + f3
f4.den = 88
f2 = f1 - f1
f3 = f1 * f1
f4 = f4 / f3

# display them again
print
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4

