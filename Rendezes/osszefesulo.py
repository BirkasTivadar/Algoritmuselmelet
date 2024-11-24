import random
import sys
import time


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
        osszefesulo(A, q + 1, r)
        osszefesul(A, p, q, r)


A = list(range(10000))
random.shuffle(A)

print(A)

start = time.time()
osszefesulo(A, 1, len(A))
end = time.time()

print(A)

print(end - start)
