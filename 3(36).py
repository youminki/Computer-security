from random import randint, seed

key = 555
seed(key)

for _ in range(10):
    value = randint(0, 100)
    print(value)