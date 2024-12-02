from kupac import *


def maximumKupacol(A, i):
    l = bal(i)
    r = jobb(i)
    print("i:", i, "l:", l, "r:", r)
    kupacMeretA = len(A) - 1
    if l <= kupacMeretA and A[l] > A[i]:
        legnagyobb = l
    else:
        legnagyobb = i

    if r <= kupacMeretA and A[r] > A[legnagyobb]:
        legnagyobb = r

    print("LEG1:", legnagyobb)
    if legnagyobb != i:
        A[i], A[legnagyobb] = A[legnagyobb], A[i]
        maximumKupacol(A, legnagyobb)


# A = [None, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
A = [None, 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]

maximumKupacol(A, 3)

print(A)
