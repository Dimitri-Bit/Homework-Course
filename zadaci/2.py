input_a = input("A: ")
input_b = input("B: ")
input_c = input("C: ")

a, b, c = int(input_a), int(input_b), int(input_c)

root_result = (b**2 - 4 * a * c) ** 0.5 # Stepenujemo sa 0.5 za korijenovanje

x1 = (-b + root_result) / 2
x2 = (-b - root_result) / 2

print(f"Root result: {root_result} \nx1: {x1} \nx2: {x2}")