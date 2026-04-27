import csv

with open('../../sample_files/passwd.csv', 'r') as f:
    reader = csv.reader(f, delimiter=':', lineterminator='\n')
    for row in reader:
        print(row)
print(csv.list_dialects())