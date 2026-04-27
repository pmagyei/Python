import csv


with open('../../sample_files/csvfile', 'a') as csvfile: #a creates a new file if
    #it doesn't exist appends data to file
    csvfile.write("") #
    writer = csv.writer(csvfile)
    csvdata = (5, 'Anne', 'Amsterdam')
    writer.writerow(csvdata)