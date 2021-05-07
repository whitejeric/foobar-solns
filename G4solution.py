# only need to think about y, find all divisors of y (X) and all multiples (Z) => number of possible luckies containing y is |X|*|Y|
# faster(?): break list down into prime factors as x|y|z => E p st. p|x,y,z (must have at least one shared prime factor)
from random import randrange
from collections import Counter
def solution(l):
    total = 0
    N = l
    X = Counter()
    Z = Counter()

    for i in  range(0,len(N)):
        y = N[i]
        div = N[:i]     #all n to the left
        mult = N[i+1:]  #all n to the right
        div = [x for x in div if y%x == 0]      #all x to the left
        mult = [z for z in mult if z%y == 0]    #all z to the right
        X[i] += len(div)
        Z[i] += len(mult)
        total += X[i]*Z[i]
    return total
