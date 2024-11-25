from teszteles import tesztelo


def feloszt(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def gyorsrendezes(A, p, r):
    if p < r:
        q = feloszt(A, p, r)
        gyorsrendezes(A, p, q - 1)
        gyorsrendezes(A, q + 1, r)


def gyorsrendezo(A):
    gyorsrendezes(A, 0, len(A) - 1)


tesztelo(gyorsrendezo, 10000)

# 1. Feladat
# A = [8, 2, 1, 5, 6, 9, 4, 3, 7]
# feloszt(A,0,8)
# print(A)

# 2. Feladat
# A = [3, 6, 2, 4, 5, 1]
# gyorsrendezes(A,0,5)
# print(A)
