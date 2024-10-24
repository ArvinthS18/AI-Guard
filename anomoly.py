import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Predefined valid values
allowed_ips = ['192.168.1.2', '192.168.1.7']
allowed_ports = [1000, 8080, 9090, 3000]
allowed_traffic_types = ['HTTP', 'SSH', 'HTTPS', 'FTP']

# Step 1: Load the CSV data
file_path = 'firewall_logs.csv'  # Replace with the actual path to your firewall_logs.csv file
df = pd.read_csv(file_path)

# Step 2: Preprocess the data
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Save original IP, port, and traffic type for output purposes
df['original_ip'] = df['ip']
df['original_port'] = df['port']
df['original_traffic_type'] = df['traffic_type']

# Encode IP addresses into numeric values using LabelEncoder
label_encoder_ip = LabelEncoder()
df['encoded_ip'] = label_encoder_ip.fit_transform(df['ip'])

# Encode traffic type
label_encoder_traffic_type = LabelEncoder()
df['encoded_traffic_type'] = label_encoder_traffic_type.fit_transform(df['traffic_type'])

# Step 3: Scale the data (but retain original IP, port, and traffic type for later display)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['encoded_ip', 'port', 'encoded_traffic_type']])

# Step 4: Train the Isolation Forest model
isolation_forest = IsolationForest(contamination=0.05, random_state=42)  # Set contamination rate as 5%
isolation_forest.fit(scaled_data)

# Step 5: Predict anomalies
df['anomaly'] = isolation_forest.predict(scaled_data)

# Step 6: Define a function to check for anomalies based on both Isolation Forest and predefined allowed values
def interpret_anomaly(row):
    # if row['anomaly'] == -1:
    #     return "Anomaly Detected: Outlier in data."
    # Direct comparison with allowed IPs, ports, and traffic types
    if row['original_ip'] not in allowed_ips:
        return "Anomaly Detected: Unusual IP address."
    if row['original_port'] not in allowed_ports:
        return "Anomaly Detected: Unusual port number."
    if row['original_traffic_type'] not in allowed_traffic_types:
        return "Anomaly Detected: Unusual traffic type."
    return "Log entry is normal."

df['anomaly_message'] = df.apply(interpret_anomaly, axis=1)

# Step 7: Filter and display any anomalies detected in the existing data, using original IP, port, and traffic type
anomalies_detected = df[df['anomaly_message'] != "Log entry is normal."]
if not anomalies_detected.empty:
    print("Anomalies Detected in the Firewall Logs:")
    print(anomalies_detected[['timestamp', 'original_ip', 'original_port', 'original_traffic_type', 'anomaly_message']])
else:
    print("No anomalies detected in the firewall logs.")

# Optionally, save the anomalies to a CSV file for further review
anomalies_detected[['timestamp', 'original_ip', 'original_port', 'original_traffic_type', 'anomaly_message']].to_csv('detected_anomalies_in_firewall_logs.csv', index=False)
