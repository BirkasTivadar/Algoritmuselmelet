import random
import time


def beszurasos(A):
    for j in range(1, len(A)):
        kulcs = A[j]
        i = j - 1
        while i >= 0 and A[i] > kulcs:
            A[i + 1] = A[i]
            i -= 1

        A[i + 1] = kulcs


A = list(range(10000))
random.shuffle(A)

print(A)

start = time.time()
beszurasos(A)
end = time.time()

print(A)

print(end - start)
