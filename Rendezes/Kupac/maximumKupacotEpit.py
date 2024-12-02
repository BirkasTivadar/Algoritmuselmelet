from maximumKupacol import maximumKupacol


def maximumKupacotEpit(A):
    kupacMeret = len(A)
    for i in range(kupacMeret // 2, 0, -1):
        maximumKupacol(A, i)


# A = [8, 2, 1, 5, 6, 9, 4, 3, 7]
# maximumKupacotEpit1(A)
# print(A)
#
# A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
# maximumKupacotEpit1(A)
# print(A)
