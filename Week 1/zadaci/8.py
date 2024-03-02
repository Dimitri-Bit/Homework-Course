area_input = input("Area: ")

area = float(area_input)
radius = (area / 3.14) ** 0.5
circumference = 3.14 * 2 * radius

print(f"Circumference: {circumference}")