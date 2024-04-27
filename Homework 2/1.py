import random

random_num = random.randint(1, 10000)

if random_num % 2 == 0:
    print(f"{random_num} even")
else:
    print(f"{random_num} odd")