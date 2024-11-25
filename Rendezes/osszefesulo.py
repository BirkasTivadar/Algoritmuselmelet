import sys
from teszteles import tesztelo


def osszefesul(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(n1):
        L.insert(i, A[p + i - 1])
    for j in range(n2):
        R.insert(j, A[q + j])
    L.insert(n1 + 1, sys.maxsize)
    R.insert(n2 + 1, sys.maxsize)
    i = 0
    j = 0
    for k in range(p - 1, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def osszefesulo(A, p, r):
    if p < r:
        q = (p + r) // 2
        osszefesulo(A, p, q)
        # print('1', A)
        osszefesulo(A, q + 1, r)
        # print('2', A)
        osszefesul(A, p, q, r)
        # print('3', A)


def osszefesules(A):
    osszefesulo(A, 1, len(A))

tesztelo(osszefesules, 10000)


# Feladat
# A = [8, 11, 5, 10, 2, 1, 9, 6, 7, 4, 3]
# osszefesules(A)


