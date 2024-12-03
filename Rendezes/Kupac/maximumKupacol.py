from kupac import *


def maximumKupacol(A, i, kupacmeretA):
    # A.insert(0, None)
    l = bal(i)
    r = jobb(i)
    if l <= kupacmeretA and A[l] > A[i]:
        legnagyobb = l
    else:
        legnagyobb = i

    if r <= kupacmeretA and A[r] > A[legnagyobb]:
        legnagyobb = r

    if legnagyobb != i:
        A[i], A[legnagyobb] = A[legnagyobb], A[i]
        maximumKupacol(A, legnagyobb, kupacmeretA)
    # A.pop(0)

# A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
# maximumKupacol(A, 3, len(A))
# print(A)
#
# A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
#
# maximumKupacol(A, 3, len(A))
# print(A)
