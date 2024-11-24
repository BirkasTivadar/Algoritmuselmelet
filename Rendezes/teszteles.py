import random
import time


def tesztelo(fuggveny, elemszam):
    A = list(range(elemszam))
    random.shuffle(A)

    print(A)

    start = time.time()
    fuggveny(A)
    end = time.time()

    print(A)

    print(end - start)