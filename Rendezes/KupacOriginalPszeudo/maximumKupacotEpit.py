from maximumKupacol import *


def maximumKupacotEpit(A):
    kupacmeretA = len(A) - 1
    for i in range(kupacmeretA // 2, 0, -1):
        # print(A)
        maximumKupacol(A, i, kupacmeretA)


# A = [None, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
# A = [None, 8, 2, 1, 5, 6, 9, 4, 3, 7]

# maximumKupacotEpit(A)
# print(A)
