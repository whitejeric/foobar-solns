def solution(xs):
    # product of array of integers
    xs.sort()
    mid = 0 # mid point for combination neg/pos
    max = xs[0]
    for m in xs:
        if m > max:
            max = m
    xs = [i for i in xs if i != 0]
    if max == 0 and (not xs or len(xs) == 1):
        return "0"
    for i in range(0, len(xs)):
        if xs[i] > 0:
            mid = i
            break
    mid_par = mid % 2 # parity of mid split aka parity of negative numbers
    mult = xs[0]
    if mid_par == 1: #odd num neg numbers
        xs[mid-1] = 1   # make last negative number 1 if odd num negatives
    for j in range(1, len(xs)):
        mult = mult*xs[j]
    return str(mult)
