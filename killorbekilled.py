#KILL OR BE KIILED

import random
import time

balas_reales = random.randint(1,5)
balas_falsas = 6 - balas_reales

print("Las balas seran las siguientes:")

for _ in range(balas_reales):
    print("V", end="")
    time.sleep(1)

# _ = 0

for _ in range(balas_falsas):
    print("F", end="")
    time.sleep(1)

print("")

print("Revolviendo balas", end="")
print(".", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")
