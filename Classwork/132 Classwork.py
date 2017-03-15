#classwork covered in 132
from random import randint
from math import pi

offices = {"jones": 123, "james": 124, "josh": 125, "joshua": 126}

for k in offices.keys():
    print k, "->", offices[k]

for k, v in offices.iteritems():
    print k, "->", v
