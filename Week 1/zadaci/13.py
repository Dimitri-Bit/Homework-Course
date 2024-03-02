tree_x_input = input("x1 coordinate: ")
tree_y_input = input("y1 coordinate: ")

house_x_input = input("x2 coordinate: ")
house_y_input = input("y2 coordinate: ")

tree_x, tree_y, house_x, house_y = int(tree_x_input), int(tree_y_input), int(house_x_input), int (house_y_input)

treasure_x = house_x + 2
treasure_y = house_y - 3

distance_tree_treasure = ((treasure_x - tree_x) ** 2 + (treasure_y - tree_y) ** 2) ** 0.5
distance_tree_house = ((house_x - tree_x) ** 2 + (house_y - tree_y) ** 2) ** 0.5
distance_house_treausre = ((treasure_x - house_x) ** 2 + (treasure_y - house_y) ** 2) ** 0.5

print(f"Treausre coordinates: ({treasure_x}, {treasure_y})")
print(f"Air distance between tree & treasure {distance_tree_treasure}")
print(f"Distance from tree to treausre while stopping by the house {distance_tree_house + distance_house_treausre}")