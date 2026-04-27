mac_list = []
with open('../../../Smoke/sample_files/macs.txt', 'r') as file:
    mac = file.read().split()
    print(mac)

    mac = list(set(mac))
    print(mac)
    for mc in mac:
        print(mc)