# with open('./newdir/devices.txt') as f:
#     print(f.readlines())

# with open('./newdir/devices.txt') as f:
#     print(f.readlines())
#     print(f.readline())


# with open('./newdir/devices.txt') as f:
#     content = f
#     print(list(list(content)))

device_list = []
with open('../../sample_files/devices.txt', ) as f:
    content = f.read().splitlines()
    for line in content[1:]:
        device_list.append(line.split(':'))
print(device_list)



# for devices in device_list:
#     print(f"pinging {devices[1]}")