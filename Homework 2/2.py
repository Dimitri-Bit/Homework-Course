import random

p = None
m = None

while True:
    p = random.randint(1, 500)
    m = random.randint(1, 500)

    if not p == m:
        break

if p > m:
    print("Petar je ubrao vise jabuka")
else:
    print("Milos je ubrao vise jabuka")