def multiply_nums(list):
    result = list[0] ** len(list)
    return result

def longest_sequence(list):
    list.append("end")

    best_value = 0
    best_sub_list = []

    sub_list = []
    last_value = list[0]

    for i in list:

        if i == last_value:
            sub_list.append(i)
        elif i == "end" or i != last_value:
            value = multiply_nums(sub_list)
            if value > best_value:
                best_value = value
                best_sub_list = sub_list.copy()

            sub_list.clear()
            sub_list.append(i)
            last_value = i
            

    return (best_value, best_sub_list)


print(longest_sequence([1, 1, 2, 2, 4, 4]))