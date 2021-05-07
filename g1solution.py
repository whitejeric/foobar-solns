from math import sqrt as sq
def solution(i):
    #prime string, get 5 digits
    #soln
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    primestr = "2357111317192329"
    num = 31
    while len(primestr) < i+5:
        if not testprime(num, primes):
            num += 2
        else:
            primes.append(num)
            primestr += str(num)
            num += 2
    return str(primestr[i:i+5])

def testprime(n, arr):
    s = sq(n)
    s_flr = 0
    for i in range(0, len(arr)-1):
        if arr[i] > s:
            s_flr = i - 1
    for j in range(0, s_flr):
        if (n % arr[j]) == 0:
            return False
    return True
