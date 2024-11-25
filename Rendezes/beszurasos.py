from teszteles import tesztelo


def beszurasos(A):
    for j in range(1, len(A)):
        kulcs = A[j]
        i = j - 1
        # print(A)
        while i >= 0 and A[i] > kulcs:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = kulcs
    # print(A)

tesztelo(beszurasos, 10000)

# Feladat
# A = [8, 2, 1, 5, 6, 9, 4, 3, 7]
# beszurasos(A)
