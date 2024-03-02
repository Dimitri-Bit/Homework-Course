x1_input = input("x1: ")
y1_input = input("y1: ")

x2_input = input("x2: ")
y2_input = input("y2: ")

x1, y1 = int(x1_input), int(y1_input)
x2, y2 = int(x2_input), int(y2_input)

x3 = (x1 + x2) / 2
y3 = (y1 + y2) / 2

d = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

print(f"The meeting spot is {x3}, {y3}")
print(f"The distance the students must travel is {d}")