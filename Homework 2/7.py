def determine_winner(math_points_1, programming_points_1, math_points_2, programming_points_2):
    total_points_1 = math_points_1 + programming_points_1
    total_points_2 = math_points_2 + programming_points_2
    
    if total_points_1 > total_points_2:
        return 1
    elif total_points_1 < total_points_2:
        return 2
    else:
        if programming_points_1 > programming_points_2:
            return 1
        elif programming_points_1 < programming_points_2:
            return 2
        else:
            return 0

math_points_1 = int(input("math points for contestant 1: "))
programming_points_1 = int(input("programming points for contestant 1: "))
math_points_2 = int(input("math points for contestant 2: "))
programming_points_2 = int(input("programming points for contestant 2: "))

winner = determine_winner(math_points_1, programming_points_1, math_points_2, programming_points_2)

if winner == 1:
    print("1 is the winner")
elif winner == 2:
    print("2 is the winner")
else:
    print("tie")
