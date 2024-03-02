d_input = input("Length (m): ")
s_input = input("Width (m): ")
r_input = input("Distance from court (m): ")

d, s, r = float(d_input), float(s_input), float(r_input)

d += r
s += r

fence_length = 2 * (d + s)

print(f"The fence should be {fence_length} meters long")