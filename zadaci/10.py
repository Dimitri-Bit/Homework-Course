x1_input = input("x1 coordinate: ")
y1_input = input("y1 coordinate: ")

x2_input = input("x2 coordinate: ")
y2_input = input("y2 coordinate: ")

x1, y1, x2, y2 = int(x1_input), int(y1_input), int(x2_input), int (y2_input)

width = abs(x2 - x1)
height = abs(y2 - y1)

area = width * height
circumference = 2 * (width + height)

print(f"Area: {area} Circumference {circumference}")