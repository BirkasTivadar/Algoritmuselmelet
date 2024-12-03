from maximumKupacol import *


def maximumKupacotEpit(A):
    # A.insert(0,None)
    kupacmeretA = len(A) - 1
    for i in range(kupacmeretA // 2, 0, -1):
        # print(A)
        maximumKupacol(A, i, kupacmeretA)
    # A.pop(0)

# A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
# maximumKupacotEpit(A)
# print(A)
#
# A = [8, 2, 1, 5, 6, 9, 4, 3, 7]
#
# maximumKupacotEpit(A)
# print(A)
