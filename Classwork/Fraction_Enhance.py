# defines a fraction
class Fraction(object):
    # by default fraction is 0/1
    def __init__(self, num = 0, den = 1):
        self.num = num
        # make sure not to set the denominatior to zero if specified
        if den == 0:
            den = 1
        self.den = den
        self.reduce()
    # getter for the numerator
    @property
    def num(self):
        return self._num

    # setter for the numerator
    @num.setter
    def num(self, value):
        self._num = value

    # getter for the denominator
    @property
    def den(self):
        return self._den

    # setter for the denominator
    @den.setter
    def den(self, value):
        # ignore if the specified denominator is 0
        if value != 0:
            self._den = value

    # returns a fractions numeric representation
    def getReal(self):
        return float(self.num) / self.den

    # String representation of the class
    def __str__(self):
        return "{}/{} ({})".format(self.num, self.den, self.getReal())

    # reduces a fraction
    def reduce(self):
        gcd = 1
        # assume smaller number is numerator
        min = self.num

        # check if the denominator is smaller
        if self.den < self.num:
            min = self.den

        # find the common divisor
        for i in range(2, min + 1):
            # when we find one update the GCD
            if self.num % i == 0 and self.den % i == 0:
                gcd = i

        # divides the numerator and the denominator by the GDC
        self.num /= gcd
        self.den /= gcd

        # if the numerator is 0, set the denominator to 1
        if self.num == 0:
            self.den = 1
    # calculates and returns the sum of two fractions
    def add(self, other):
        num = (self.num * other.den) + (other.num * self.den)
        den = self.den * other.den
        sum = Fraction(num, den)
        sum.reduce()
        return sum
# main program
f1 = Fraction(1, 2)
f2= Fraction(1, 4)
f3 = f1.add(f2)

print f1
print f2
print f3

