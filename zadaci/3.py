# a^2 - b^2 = (a - b) * (a + b)

a_input = input("A (Squared): ")
b_input = input("B (Squared): ")

a, b = int(a_input), int(b_input)

result = (a - b) * (a + b)

print(f"Result: {result}")