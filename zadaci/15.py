ax_input = input("X coordinate of A: ")
ay_input = input("Y coordinate of A: ")

bx_input = input("X coordinate of B: ")
by_input = input("Y coordinate of B: ")

cx_input = input("X coordinate of C: ")
cy_input = input("Y coordinate of C: ")

ax, ay = int(ax_input), int(ay_input)
bx, by = int(bx_input), int(by_input)
cx, cy = int(cx_input), int(cy_input)

ab = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
cb = ((bx - cx) ** 2 + (by - cy) ** 2) ** 0.5
ca = ((cx - ax) ** 2 + (cy - ay) ** 2) ** 0.5

s = (ab + cb + ca) / 2
area = (s * (s - ab) * (s - cb) * (s - ca)) ** 0.5

print(f"ab: {ab} \ncb: {cb} \nca: {ca}")
print(f"Area: {area}")