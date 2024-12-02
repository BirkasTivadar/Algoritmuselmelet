from kupac import *


def maximumKupacol(A, i):
    l = bal(i)
    r = jobb(i)
    kupacmeretA = len(A)
    l -= 1
    r -= 1
    i -= 1

    if l < kupacmeretA and A[l] > A[i]:
        legnagyobb = l
    else:
        legnagyobb = i

    if r < kupacmeretA and A[r] > A[legnagyobb]:
        legnagyobb = r

    if legnagyobb != i:
        A[i], A[legnagyobb] = A[legnagyobb], A[i]
        maximumKupacol(A, legnagyobb + 1)


# A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
#
# maximumKupacol(A, 3)
# print(A)
