num = input("Enter six digit number: ")

a = int(num[0])
b = int(num[1])
c = int(num[2])
d = int(num[3])
e = int(num[4])
f = int(num[5])

sqrt = (a + b + c + d + e + f) ** 2
result = sqrt - (c * d)

print(f"Identification number {result}")