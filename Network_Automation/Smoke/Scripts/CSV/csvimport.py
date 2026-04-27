import csv

with open('./sample_files/airtravel.csv', 'r') as f:
    csv_file = csv.reader(f)
    next(csv_file)  #removes the header
    year = dict()
    for line in csv_file:
        year[line[0]] = line[1]
    print(year)

    max_year = max(year.values())
    print(max_year)

    for k, v in year.items():
        if max_year == v:
            print(f"{k}, {v}")