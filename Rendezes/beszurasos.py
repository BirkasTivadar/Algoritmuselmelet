from teszteles import tesztelo


def beszurasos(A):
    for j in range(1, len(A)):
        kulcs = A[j]
        i = j - 1
        while i >= 0 and A[i] > kulcs:
            A[i + 1] = A[i]
            i -= 1

        A[i + 1] = kulcs


tesztelo(beszurasos)
