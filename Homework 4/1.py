from functools import reduce

def longest_string(list):
    return reduce(lambda x, y: x if len(x) > len(y) else y, list)

list_of_strings = ["flower", "flow", "flight"]
print("Longest String:", longest_string(list_of_strings))
