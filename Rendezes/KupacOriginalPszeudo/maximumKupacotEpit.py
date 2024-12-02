from maximumKupacol import *


def maximumKupacotEpit(A):
    kupacmeretA = len(A) - 1
    for i in range(kupacmeretA // 2, 0, -1):
        maximumKupacol(A, i)


A = [None, 8, 2, 1, 5, 6, 9, 4, 3, 7]

maximumKupacotEpit(A)
print(A)
