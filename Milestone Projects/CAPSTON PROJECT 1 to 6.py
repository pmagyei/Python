# A dictionary mapping server names to their environments
server_environments = {
    'web-01': 'production',
    'db-01': 'production',
    'test-01': 'staging',
    'dev-01': 'development'
}

# A list of dictionaries, where each dictionary is a security alert
incoming_alerts = [
    {'id': 'A001', 'severity': 'high', 'source_ip': '192.168.1.50', 'target': 'web-01'},
    {'id': 'A002', 'severity': 'low', 'source_ip': '10.0.0.5', 'target': 'dev-01'},
    {'id': 'A003', 'severity': 'critical', 'source_ip': '203.0.113.42', 'target': 'db-01'},
    {'id': 'A004', 'severity': 'high', 'source_ip': '198.51.100.23', 'target': 'test-01'}
]

# An empty list to store the IP addresses we need to block
blocked_ips = []
current_env = {}
for security_alert in incoming_alerts:

    for environments in server_environments.values():
        current_env = { security_alert['target']: environments,}

print(current_env)
