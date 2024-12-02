from maximumKupacotEpit import *


def kupacRendezes(A):
    maximumKupacotEpit(A)
    kupacmeretA = len(A)
    for i in range(kupacmeretA - 1, 1, -1):
        print(A[0])
        A[0], A[i] = A[i], A[0]
        kupacmeretA -= 1
        maximumKupacol(A, i)


A = [8, 2, 1, 5, 6, 9, 4, 3, 7]

kupacRendezes(A)
print(A)
