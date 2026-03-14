import csv

RANDOM_FILE_NAME = "random.csv"
MICHAELS_FILE_NAME = "random-michaels.csv"
RESULT_FILE_NAME = "result_trokoz.csv"

def read_csv(filename: str) -> list:
    data = []

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(tuple(row))

    return data

def write_csv(filename: str, data: list) -> None:
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

data_1 = read_csv(MICHAELS_FILE_NAME)
data_2 = read_csv(RANDOM_FILE_NAME)
unique_data = list(set(data_1 + data_2))
write_csv(RESULT_FILE_NAME, unique_data)





