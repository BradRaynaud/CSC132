# full adder

def fullAdder(A, B, C):
    TT = {(0, 0, 0): (0, 0),
          (0, 0, 1): (0, 1),
          (0, 1, 0): (0, 1),
          (0, 1, 1): (1, 0),
          (1, 0, 0): (0, 1),
          (1, 0, 1): (1, 0),
          (1, 1, 0): (1, 0),
          (1, 1, 1): (1, 1), }

    return TT[(A, B, C)]


def fullAdderEQ(A, B, C):
    K = (not A and B and C) or (A and not B and C) or (A and B and not C) or (A and B and C)
    # K = A'BC + AB'C + ABC' + ABC
    S = (not A and not B and C) or (not A and B and not C) or (A and not B and not C) or (A and B and C)
    # S = A'B'C + A'BC' + AB'C' + ABC

    return "({}, {})".format(K, S)


# testing
print(fullAdder(1, 0, 1))
print(fullAdderEQ(1, 0, 1))
