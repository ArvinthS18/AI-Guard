import pandas as pd

# Path to your CSV log file
# csv_file = 'C:/Users/A7765/AI/withbreach.csv'  # Replace with the actual path to your CSV file
csv_file = 'C:/Users/A7765/AI/firewall_logs.csv'
# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Convert the timestamp to a datetime object
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Sort the DataFrame by IP, port, and timestamp
df = df.sort_values(by=['ip', 'port', 'timestamp'])

# Group by IP and port to analyze action sequences
grouped = df.groupby(['ip', 'port'])

# Initialize list to hold potential breaches
potential_breaches = []

# Analyze each group for DENY followed by ALLOW sequences
for name, group in grouped:
    deny_count = 0
    for idx, row in group.iterrows():
        if row['action'] == 'DENY':
            deny_count += 1
        elif row['action'] == 'ALLOW' and deny_count >= 2:  # Detect breach after multiple DENY
            potential_breaches.append(row)
            deny_count = 0  # Reset count after breach is detected
        else:
            deny_count = 0  # Reset count if sequence is broken

# Check and display breaches
if potential_breaches:
    # Print the breaches in the desired format
    for breach in potential_breaches:
        print("Potential network breaches detected:")
        print("timestamp,ip,port,traffic_type,action")
        print(f"{breach['timestamp']},{breach['ip']},{breach['port']},{breach['traffic_type']},{breach['action']}")
else:
    print("No potential network breaches detected.")
