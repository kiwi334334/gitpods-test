import random


def rand():
    while True:
        x = random.randrange(0, 101)
        print(x)
        if x == 100:
            break
