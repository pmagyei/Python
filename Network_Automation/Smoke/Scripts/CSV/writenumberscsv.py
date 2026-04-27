import csv


with open('../../sample_files/numberstable.csv', 'w') as f: # if there are spaces after each line add: newline='' as an argument
    writer = csv.writer(f)
    writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
    for x in range(1, 101):
        writer.writerow([x, x**2, x**3, x**4])