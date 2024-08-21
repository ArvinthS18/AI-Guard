import csv
import time
import random
from datetime import datetime

# Firewall rules
rules_file = 'rules.csv'
log_file = 'firewall_logs.csv'

# Sample IPs, ports, and traffic types for data generation
ips = ['192.168.1.2', '192.168.1.7']
ports = [1000, 8080, 9090, 3000]
traffic_types = ['HTTP', 'SSH', 'HTTPS', 'FTP']


# ips = ['192.168.1.2', '192.168.1.7', '192.168.2.5', '192.168.2.9', '10.0.0.1', '10.0.0.2', '172.16.0.1', '172.16.0.2']
# ports = [1000, 8080, 9090, 3000, 443, 80, 22, 21, 25, 3306]
# traffic_types = ['HTTP', 'SSH', 'HTTPS', 'FTP', 'SMTP', 'MySQL', 'IMAP', 'POP3', 'SNMP', 'SFTP']


# Read rules from CSV file
def read_rules(rules_file):
    rules = []
    with open(rules_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rules.append(row)
            print(rules)
    return rules

# Firewall function to allow or deny traffic based on rules
def firewall(ip, port, traffic_type, rules):
    for rule in rules:
        if rule['ip'] == ip and int(rule['port']) == port and rule['traffic_type'] == traffic_type:
            return rule['action']
    return 'DENY'

# Generate random traffic data
def generate_traffic_data():
    ip = random.choice(ips)
    port = random.choice(ports)
    traffic_type = random.choice(traffic_types)
    return ip, port, traffic_type

# Log the traffic data
def log_traffic_data(log_file, timestamp, ip, port, traffic_type, action):
    with open(log_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, ip, port, traffic_type, action])

# Main function
def main():
    rules = read_rules(rules_file)
    
    # Write headers to the log file
    with open(log_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp', 'ip', 'port', 'traffic_type', 'action'])
    
    while True:
        ip, port, traffic_type = generate_traffic_data()
        action = firewall(ip, port, traffic_type, rules)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_traffic_data(log_file, timestamp, ip, port, traffic_type, action)
        print(f"{timestamp} - IP: {ip}, Port: {port}, Traffic Type: {traffic_type}, Action: {action}")
        time.sleep(2)

if __name__ == "__main__":
    main()
