import pandas as pd

# Load the CSV file
log_file = r'C:\Users\A7765\AI\firewall_logs.csv'

# Load the data
logs = pd.read_csv(log_file)

# Strip any extra whitespace from column names
logs.columns = logs.columns.str.strip()

# Convert 'timestamp' to datetime
logs['timestamp'] = pd.to_datetime(logs['timestamp'], errors='coerce', format='%Y-%m-%d %H:%M:%S')

# Drop rows with invalid timestamps
logs = logs.dropna(subset=['timestamp'])

# Encode 'action' column (DENY -> 0, ALLOW -> 1)
logs['action'] = logs['action'].apply(lambda x: 0 if x == 'DENY' else 1)

# Breach Detection Logic
def detect_breaches(logs):
    breach_logs = {}

    # 1. Repeated DENY Detection
    repeated_denies = logs[(logs['action'] == 0)].groupby(['ip', 'port', 'traffic_type']).size()
    repeated_denies = repeated_denies[repeated_denies > 2]
    if not repeated_denies.empty:
        breach_logs['Repeated DENY Detection'] = repeated_denies

    # 2. Protocol Change Detection
    protocol_changes = []
    for ip_port, group in logs.groupby(['ip', 'port']):
        if group['traffic_type'].nunique() > 1 and (group['action'] == 0).any():
            protocol_changes.append((ip_port, group))
    if protocol_changes:
        breach_logs['Protocol Change Detection'] = protocol_changes

    # 3. ALLOW After DENY Detection
    allow_after_deny = []
    for ip_port, group in logs.groupby(['ip', 'port']):
        deny_count = (group['action'] == 0).sum()
        if deny_count >= 2 and group.iloc[-1]['action'] == 1:
            allow_after_deny.append((ip_port, group))
    if allow_after_deny:
        breach_logs['ALLOW After DENY Detection'] = allow_after_deny

    # 4. Unusual Port Usage Detection (e.g., 8080, 9090, 3000)
    unusual_ports = logs[(logs['port'].isin([8080, 9090, 3000])) & (logs['action'] == 0)]
    if not unusual_ports.empty:
        breach_logs['Unusual Port Usage Detection'] = unusual_ports

    return breach_logs

# Detect breaches
breaches = detect_breaches(logs)

# Format and print the structured output
def print_breaches(breaches):
    if breaches:
        for breach_type, data in breaches.items():
            print(f"\n{'='*50}\n{breach_type}\n{'='*50}")
            
            if breach_type == 'Repeated DENY Detection':
                print(data.to_string())
            
            elif breach_type == 'Protocol Change Detection':
                for ip_port, group in data:
                    print(f"\nIP: {ip_port[0]}, Port: {ip_port[1]}")
                    print(group[['timestamp', 'ip', 'port', 'traffic_type', 'action']].to_string(index=False))
            
            elif breach_type == 'ALLOW After DENY Detection':
                for ip_port, group in data:
                    print(f"\nIP: {ip_port[0]}, Port: {ip_port[1]}")
                    print(group[['timestamp', 'ip', 'port', 'traffic_type', 'action']].to_string(index=False))
            
            elif breach_type == 'Unusual Port Usage Detection':
                print(data[['timestamp', 'ip', 'port', 'traffic_type', 'action']].to_string(index=False))
    else:
        print("No breaches detected.")

# Print breaches in a structured format
print_breaches(breaches)
