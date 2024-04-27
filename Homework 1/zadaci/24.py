x = input("X: ")
y = input("Y: ")

print(f"Results before: x \"{x}\" & y \"{y}\"")

z = x
x = y
y = z

print(f"Results after: x \"{x}\" & y \"{y}\"")