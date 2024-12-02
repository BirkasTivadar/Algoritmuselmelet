from teszteles import tesztelo


def horareFeloszt(A, p, r):
    x = A[p]
    i = p
    j = r
    while True:
        while A[j] > x:
            j -= 1
        while A[i] < x:
            i += 1
        if i < j:
            A[i], A[j] = A[j], A[i]
            # print(A)
        else:
            return j


def horareGyorsrendezes(A, p, r):
    if p < r:
        q = horareFeloszt(A, p, r)
        horareGyorsrendezes(A, p, q)
        horareGyorsrendezes(A, q + 1, r)


def horareGyorsrendezo(A):
    horareGyorsrendezes(A, 0, len(A) - 1)


tesztelo(horareGyorsrendezo, 10000)

# A = [8, 2, 1, 5, 6, 9, 4, 3, 7]
#
# horareFeloszt(A, 0, 8)
