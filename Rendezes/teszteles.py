import random
import time


def tesztelo(fuggveny):
    A = list(range(10000))
    random.shuffle(A)

    print(A)

    start = time.time()
    fuggveny(A)
    end = time.time()

    print(A)

    print(end - start)
