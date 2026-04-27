import csv

csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')

with open('../../sample_files/items.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='hashes')
    for line in reader:
        print(line)


with open('../../sample_files/items.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, dialect='hashes')
    writer.writerow(('spoon', 3, 1.5))