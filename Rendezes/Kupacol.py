def szulo(i):
    return i // 2


def bal(i):
    return 2 * i


def jobb(i):
    return (2 * i) + 1


def maximumKupacol(A, i):
    A.insert(0, None)
    l = bal(i)
    r = jobb(i)
    kupacmeretA = len(A)
    # print(A)

    if l <= kupacmeretA and A[l] > A[i]:
        legnagyobb = l
    else:
        legnagyobb = i

    if r <= kupacmeretA and A[r] > A[legnagyobb]:
        legnagyobb = r

    if legnagyobb != i:
        A[i], A[legnagyobb] = A[legnagyobb], A[i]
        A = A[1:]
        print(A)
        maximumKupacol(A, legnagyobb)


A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]

maximumKupacol(A, 3)
print(A)
