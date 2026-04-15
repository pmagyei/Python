server_inventory = {
    'web-front-01': 'Ubuntu_18',
    'database-01': 'CentOS_7',
    'auth-server': 'Ubuntu_22',
    'legacy-app': 'Windows_2012'
}

# Dictionary 2: What is the current threat level of each OS?
os_threat_levels = {
    'Ubuntu_18': 'Critical',
    'Ubuntu_22': 'Safe',
    'CentOS_7': 'High',
    'Windows_2012': 'Critical'
}

servers_at_threat = []

for server, os in server_inventory.items():
    t_level = os_threat_levels[os]
    if t_level in ['Critical', 'High']:
        servers_at_threat.append(server)
        print(f" WARNING: The current server: {server} is at a {t_level} threat.")

