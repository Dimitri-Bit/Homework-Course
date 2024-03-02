# 𝑎^2 + 𝑏^2 + 𝑐^2 + 2𝑎𝑏 + 2𝑎𝑐 + 2𝑏c
a_input = input("A: ")
b_input = input("B: ")
c_input = input("C: ")

a, b, c = int(a_input), int(b_input), int(c_input)

result = a**2 + b**2 + c**2 + 2*a*b + 2*a*c + 2*b*c

print(f"Result: {result}")