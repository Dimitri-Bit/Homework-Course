def neighbor_characters(string):
    best_value = 0
    value = 0
    last_character = ""

    for i in range(len(string)):
        if string[i] == last_character:
            value += 1
            if value > best_value:
                best_value = value
        else:
            value = 1
            last_character = string[i]

    return best_value

print(neighbor_characters("aabbb"))