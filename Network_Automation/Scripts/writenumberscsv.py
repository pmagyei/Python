import csv


with open('./sample_files/numbers.csv', 'w') as f: # if spaces after new line add: newline='' as an argument
    writer = csv.writer(f)
    writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
    for x in range(1, 101):
        writer.writerow([x, x**2, x**3, x**4])