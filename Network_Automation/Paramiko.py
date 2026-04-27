import paramiko
import time
import getpass
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #accepts the host key
# ssh_client.connect(hostname='170.170.170.10', port=22, username='admin', password='cisco0',
#                    look_for_keys=False, allow_agent=False)
#password = getpass.getpass(prompt="Enter Password: ")
router1 = {'hostname': '170.170.170.10', 'port': '22', 'username': 'admin', 'password': 'cisco0'}
router2 = {'hostname': '170.170.170.4', 'port': '22', 'username': 'admin', 'password': 'cisco0'}
router3 = {'hostname': '170.170.170.12', 'port': '22', 'username': 'admin', 'password': 'cisco0'}

routers = [router1, router2, router3]

for router in routers:
    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False) #**unpacks router dictionary

    shell = ssh_client.invoke_shell()
    shell.send('en\n')
    shell.send('cisco\n')
    shell.send('conf t\n')
    shell.send('router ospf 1\n')
    shell.send('network 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('terminal length 0\n')
    shell.send('sh ip protocols\n')
    time.sleep(1)
    output = shell.recv(10000)
    output = output.decode('utf-8')
    print(output)

    if ssh_client.get_transport().is_active() == True:
        print(f'Disconnecting from {router["hostname"]}')
        ssh_client.close() # closes connection