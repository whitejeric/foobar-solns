#if n is even divide by 2
#on either side of every odd number there is an even number divisible by 2 or 4
#if n is odd, if n%4 == 3: add 1 (divisible by 4 now) if n%4 == 1, minus 1 (divisible by 4 now)
#if n is even n%4 is either 2 or 0 => its even and would already by divided
#solution
def solution(n):
    n = int(n)
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
        elif n > 3:
            if n % 4 == 1:
                n = n -1
            else:
                n = n + 1
        else: #n = 3, we want to minus- only time
            n = n - 1
        count += 1
    return count

# print(solution('3'))
# print(solution('4'))
