def check_bee(x, y):
    wire_y = 2 * x + 5
    
    if y == wire_y:
        print("bee is moving on the wire.")
    else:
        print("bee is not moving on the wire.")

x_bee = float(input("x bee: "))
y_bee = float(input("y bee: "))

check_bee(x_bee, y_bee)