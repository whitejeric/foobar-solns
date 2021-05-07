import numpy as np
from fractions import gcd
from fractions import Fraction

def solution(m):
    terminators = find_states(m,0)
    non_terminators = find_states(m,1)
    if len(terminators) == 1:
        return [1,1]
    RQ = get_RQ(m, terminators)
    RQ = arr_to_mtx(RQ)
    m = arr_to_mtx(m)
    R = sub_RQ(RQ, terminators)
    Q = sub_RQ(RQ, non_terminators)
    I = mtx_ident(len(Q))
    I = arr_to_mtx(I)
    Q_I = mtx_sub(I,Q)
    F = mtx_inv(Q_I)
    FR = mtx_mult(F,R)
    FR_0 = []
    for f in FR[0]:
        FR_0.append(f.denominator)
    L = int(get_lcm(FR_0))
    # heres where i'd print everything
    return final(FR[0], L)

def final(F_0, L):
    result = []
    for f in F_0:
        if f.numerator == 0:
            result.append(0)
        else:
            result.append(int((f.numerator*L)/f.denominator))
    result.append(L)
    r_no_zeros = [i for i in result if i!=0]
    if len(r_no_zeros) == 2:    # only one terminal state is reachable
        for i in range(len(result)):
            if result[i] > 0:
                result[i] = 1
    return result

def lcm(x,y):
    x = int(x)
    y = int(y)
    xy = x*y
    return int(xy/gcd(x,y))

# lcm for the 0 row of FR
def get_lcm(FR_0):
    if len(FR_0) == 2:
        return lcm(FR_0[0], FR_0[1])
    if len(FR_0) == 1:
        return FR_0[0]
    L = lcm(FR_0[0], FR_0[1])
    for i in range(2, len(FR_0)):
        L = lcm(L, FR_0[i])
    return L

# gets RQ based on the terminating states
def get_RQ(m, terms):
    RQ = []
    for i in range(len(m)):
        if i not in terms:
            rq = []
            for col in m[i]:
                rq.append(col)
            RQ.append(rq)
    return RQ

# returns R or Q depending on the the indices in terms
def sub_RQ(RQ,terms):
    sub = []
    for row in RQ:
        r = []
        for t in terms:
            r.append(row[t])
        sub.append(r)
    return sub

# determines which states are terminators or regular
def find_states(m, val):
    rows = []
    if val == 0:    #find terminators
        for i in range(len(m)):
            if all(col == val for col in m[i]):
                rows.append(i)
    else:   #find non_terminators
        for i in range(len(m)):
            for j in range(len(m[i])):
                if (m[i][j] >= val):
                    rows.append(i)
                    break
    return rows

# impliments dot product multi
def mtx_mult(A,B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            row.append(Fraction())
        result.append(row)
    for i in range(len(A)): #rows of A
        for j in range(len(B[0])): #cols of B
            for k in range(len(B)): #rows of B
                x = A[i][k] * B[k][j]
                if x.denominator > 0:
                    result[i][j] += x
    return result

# only need sub, no need for add
def mtx_sub(A,B):
    result = []
    if len(A) != len(B):
        print("Mismatch error {A} sub {B}".format(A=A, B=B))
    for i in range(len(A)):
        r = []
        a = A[i]
        b = B[i]
        for j in range(0,len(A[i])):
            r.append(a[j]-b[j])
        result.append(r)
    return result

# unneccesary but works!
def mtx_permute(M, rows, cols):
    I = mtx_ident(len(M))
    # each of rows is a pair of indices [i,j] st. i will swap with j
    # ditto for cols
    for r in rows:
        i = r[0]
        j = r[1]
        temp = [n for n in I[i]]
        I[i] = [n for n in I[j]]
        I[j] = temp
    for c in cols:
        i = c[0]
        j = c[1]
        for row in I:
            temp = row[i]
            row[i] = row[j]
            row[j] = temp
    return mtx_mult(M,I)

# finds inverse via row reduction (F|I) => (I|F^-1)
# whatever we do to one we do to the other :)
# AF = I
def mtx_inv(F):
    I = mtx_ident(len(F))
    for j in range(len(F)):
        i = j
        if F[i][j] == 0:
            continue
        f_ij = F[i][j]
        rec = Fraction(1,f_ij)
        A = mtx_ident(len(F))
        A[i][i] = rec
        F = mtx_mult(A,F)
        I = mtx_mult(A,I)
        # mult both F and I at row i with reciprical of F_ii
        for l in range(len(F)):
            if i!=l:
                # i =0, j =0, l= 1
                f_lj = F[l][j]
                rec = -1*f_lj   # not really a reciprical but there was a flip!
                A = mtx_ident(len(F))
                A[l][i] = rec
                # add rec*F_i to F_j
                F = mtx_mult(A,F)
                I = mtx_mult(A,I)
    return I

# converts a regular 2d array to one we can work with (using Fractions)
def arr_to_mtx(M):
    result = []
    for row in M:
        denom = sum(row)
        if denom == 0:  #term row
            r = [Fraction()] * len(row)
            result.append(r)
        else:
            r = []
            for col in row:
                f = Fraction(col, denom)
                r.append(f)
            result.append(r)
    return result

# troubleshooting, batch printing matrices
def batch_print(list):
    for item in list:
        print(mtx_p(item[0],item[1]))

# nicish printer for a matrix with functions
def mtx_p(M, name):
    max_length = 0
    result = '{a}{b}{a}\n'.format(a='-'*15, b=name)
    col_width = max(len(str(word)) for row in M for word in row) + 2  # padding
    res = []
    for r in M:
        st = "| "
        for c in r:
            n = c.numerator
            d = c.denominator
            if n == 0 or (n == 1 and d == 1):
                st += " {b}  ".format(b = n).ljust(col_width)
            else:
                st += "{a}/{b} ".format(a = n, b = d).ljust(col_width)
        if len(st) > max_length:
            max_length = len(st)
        res.append(st)
    for s in res:
        result+=s + '|\n'
    return result

# creates an identity array
def mtx_ident(size):
    identity = np.identity(size)
    I = []
    for row in identity:
        r = []
        for col in row:
            if col > 0:
                r.append(Fraction(1,1))
            else:
                r.append(Fraction())
        I.append(r)
    return I


# print_list = [[m,'m'],[RQ, 'RQ'],[R,'R'],[Q,'Q'],[Q_I, 'Q_I'],[F, 'F'],[FR, 'FR']]
# batch_print(print_list)
# print(final(FR[0], L))

# print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
# print(solution([[ 4, 3, 9, 5, 2, 7, 1, 0],
# [ 7, 4, 0, 6, 4, 9, 8, 5],
# [ 8, 7, 7, 0, 8, 1, 9, 7],
# [ 6, 3, 9, 8, 9, 9, 5, 9],
# [ 5, 5, 5, 5, 8, 6, 3, 4],
# [ 0, 4, 2, 5, 1, 6, 4, 5],
# [ 0, 0, 0, 0, 0, 0, 0, 0],
# [ 0, 0, 0, 0, 0, 0, 0, 0]]))
# print(solution([[0, 2, 1, 0, 0],
#             [0, 0, 0, 3, 4],
#             [0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0]]))
#
# print(solution([[0, 1, 0, 0, 0, 1],
#             [4, 0, 0, 3, 2, 0],
#             [0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0]]))
#
# print(solution([[0, 1, 0, 0, 0, 1],
#             [1, 0, 0, 1, 1, 0],
#             [0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0]]))
#
# print(solution([[1, 1, 0, 1],
#             [1, 1, 0, 0],
#             [0, 0, 0, 0],
#             [0, 0, 0, 0]]))
#
# print(solution([[0, 0, 0, 0],
#             [1, 1, 1, 1],
#             [1, 1, 1, 1],
#             [1, 1, 1, 1]]))
# print(solution([[ 397, 492, 732, 484, 399, 244, 324, 150],
# [ 504, 788, 968, 468, 882, 224, 763, 323],
# [ 757, 466, 870, 29, 731, 33, 441, 375],
# [ 496, 442, 190, 795, 742, 740, 616, 939],
# [ 114, 784, 925, 289, 467, 53, 429, 742],
# [ 879, 703, 649, 73, 500, 916, 910, 827],
# [ 0, 0, 0, 0, 0, 0, 0, 0],
# [ 0, 0, 0, 0, 0, 0, 0, 0]]))
