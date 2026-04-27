import csv

device_list = []
with open('../sample_files/networkdevices.txt') as f:
    devices = f.read().splitlines() # reads file into a list
    for line in devices[1:]: #line=lines in the file(devices)
        #print(line)
        device_list.append(line.split(':')) # appending each line as a list within a list every :
print(type(device_list))  # list

#write to .txt file
with open('../sample_files/networkdevicesinfo.txt', 'w') as networkdevicesinfo: # if there are spaces after each line add: newline='' as an argument
    networkdevicesinfo.write(str(device_list))  #converts list into str value

#writes to csv file
with open('../sample_files/networkdevicesinfo.csv', 'w') as ndicsv:
    ndicsv.write("")
    writer = csv.writer(ndicsv)
    csvdata = device_list
    writer.writerow(csvdata)

