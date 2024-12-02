from maximumKupacotEpit import *


def kupacRendezes(A):
    maximumKupacotEpit(A)
    kupacmeretA = len(A) - 1
    for i in range(len(A)-1, 0, -1):
        print(A[1])
        A[1], A[i] = A[i], A[1]
        kupacmeretA -= 1
        maximumKupacol(A, 1, kupacmeretA)


A = [None, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

kupacRendezes(A)
print(A)
