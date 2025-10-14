import csv
def load_data_from_csv(csv_file):
    data_list = []
    with open(csv_file, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            if not row:
                continue
            date = row[0]
            min = int(row[1])
            max = int(row[2])
            data_list.append([date, min,max])
    return data_list 


# dataset here as a string
dataset = """date,min,max
2020-06-19T07:00:00+08:00,47,46
2020-06-20T07:00:00+08:00,51,67
2020-06-21T07:00:00+08:00,58,72
2020-06-22T07:00:00+08:00,59,71
2020-06-23T07:00:00+08:00,52,71
2020-06-24T07:00:00+08:00,52,67
2020-06-25T07:00:00+08:00,48,66
2020-06-26T07:00:00+08:00,53,66
"""

# Print the result directly
print(load_data_from_csv(dataset))
