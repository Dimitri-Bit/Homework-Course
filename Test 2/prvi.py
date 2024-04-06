import csv

def highest_value(csv, column):
    highest_value = 0

    for row in csv:
        value = row[column]
        if value.isnumeric():
            highest_value = max(int(value), highest_value)

    return highest_value

def average_value(csv, column):
    total_value = 0
    count = 0

    for row in csv:
        value = row[column]
        if value.isnumeric():
            total_value = total_value + int(value)
            count = count + 1

    return (total_value / count)
            
def difference_in_percentage(a, b):
    result = abs((a-b)/(a+b)/2) * 100
    return round(result)

def normalize_column(csv, column, devision):
    for row in csv:
        value = row[column]
        if value.isnumeric():
            row[column] = int(value) / devision
    return csv


with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    file = list(csv_reader)

    highest_value = highest_value(file, 1)
    average_value = average_value(file, 1)
    difference_in_percentage = difference_in_percentage(highest_value, average_value)

    print(f"Highest value: {highest_value}")
    print(f"Average value: {average_value}")
    print(f"Difference in percentage: {difference_in_percentage}%")

    normalize_column(file, 1, highest_value)


    
