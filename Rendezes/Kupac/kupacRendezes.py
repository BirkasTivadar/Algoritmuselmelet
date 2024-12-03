from maximumKupacotEpit import *


def kupacRendezes(A):
    A.insert(0, None)
    maximumKupacotEpit(A)
    kupacmeretA = len(A) - 1
    for i in range(len(A) - 1, 0, -1):
        A[1], A[i] = A[i], A[1]
        kupacmeretA -= 1
        maximumKupacol(A, 1, kupacmeretA)

    A.pop(0)


A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

kupacRendezes(A)
print(A)
