import csv

dataset_file_name = 'dataset.csv'
column_num = 1

def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def get_dataset():
    with open(dataset_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)
    
def write_dataset(dataset):
    writer = csv.writer(open(dataset_file_name, 'w'))
    writer.writerows(dataset)

def get_highest_value(csv, column):
    highest_value = 0

    for row in csv:
        value = row[column]
        if value.isdigit() or is_float(value):
            highest_value = max(float(value), highest_value)

    return highest_value

def get_lowest_value(csv, column):
    lowest_value = 999999

    for row in csv:
        value = row[column]
        if value.isdigit() or is_float(value):
            lowest_value = min(float(value), lowest_value)

    return lowest_value

def get_average_value(csv, column):
    total_value = 0
    count = 0

    for row in csv:
        value = row[column]
        if value.isdigit() or is_float(value):
            total_value += float(value)
            count += 1

    return total_value / count

def normalize_column(csv, column, devision):
    for row in csv:
        value = row[column]
        if value.isdigit() or is_float(value):
            row[column] = float(value) / devision

    return csv

# Fromula: |(a-b)/(a+b)| * 100%
def get_difference_in_percentage(a, b):
    return abs((a-b)/(a+b) * 100)

dataset = get_dataset()
highest_value = get_highest_value(dataset, column_num)
lowest_value = get_lowest_value(dataset, column_num)
average_value = get_average_value(dataset, column_num)
difference = get_difference_in_percentage(highest_value, average_value)
normalized_dataset = normalize_column(dataset, column_num, highest_value)
write_dataset(normalized_dataset)

print(f"Highest Value: {round(highest_value, 2)} \nLowest Value: {round(lowest_value, 2)} \nAverage Value: {round(average_value, 2)} \nDifference: {round(difference, 2)}%")