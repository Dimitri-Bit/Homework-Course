a_input = input("Length (in mm): ")
b_input = input("Width (in mm): ")

a, b = int(a_input), int(b_input)
a, b = a / 10, b / 10 # Convert to cm

area = a * b

print(f"Area: {area}cm^2")
