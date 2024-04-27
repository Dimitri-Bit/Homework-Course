def calculate_performance(average):
    if average >= 4.5:
        return "Excellent"
    elif average >= 3.5:
        return "Very good"
    elif average >= 2.5:
        return "Good"
    elif average >= 2:
        return "Sufficient"
    else:
        return "Insufficient"

grades = input("student's grades ").split()
grades = [1 if grade.upper() == 'F' else int(grade) for grade in grades]

average_grade = sum(grades) / len(grades)
performance = calculate_performance(average_grade)

print("student's performance is:", performance)
