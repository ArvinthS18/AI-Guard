# import pandas as pd
# from sklearn.ensemble import IsolationForest

# # Load the log data from a CSV file
# df = pd.read_csv('firewall_logs.csv')

# # Converting timestamp to datetime
# df['timestamp'] = pd.to_datetime(df['timestamp'])

# # Encoding categorical variables
# df['traffic_type'] = df['traffic_type'].astype('category').cat.codes
# df['ip'] = df['ip'].astype('category').cat.codes

# # Selecting features for anomaly detection
# features = ['ip', 'port', 'traffic_type']

# # Applying Isolation Forest for anomaly detection
# model = IsolationForest(contamination=0.1, random_state=42)
# df['anomaly'] = model.fit_predict(df[features])

# # Identifying and displaying anomalies
# anomalies = df[df['anomaly'] == -1]

# # Save anomalies to a CSV file
# anomalies.to_csv('anomalies_detected.csv', index=False)

# print("Anomalies detected and saved to 'anomalies_detected.csv'")



# import pandas as pd
# from sklearn.ensemble import IsolationForest
# from sklearn.preprocessing import LabelEncoder, StandardScaler

# # Step 1: Load the CSV data
# file_path = 'firewall_logs.csv'  # Replace with the actual path to your rules.csv file
# df = pd.read_csv(file_path)

# # Step 2: Preprocess the data

# # Convert timestamp into numerical values (UNIX timestamp)
# df['timestamp'] = pd.to_datetime(df['timestamp']).astype(int) / 10**9  # Convert to UNIX timestamp

# # Convert categorical columns to numerical values using LabelEncoder
# label_encoders = {}
# for column in ['ip', 'traffic_type', 'action']:
#     label_encoders[column] = LabelEncoder()
#     df[column] = label_encoders[column].fit_transform(df[column])

# # Step 3: Scale the data
# scaler = StandardScaler()
# scaled_data = scaler.fit_transform(df[['timestamp', 'ip', 'port', 'traffic_type', 'action']])

# # Step 4: Train Isolation Forest
# isolation_forest = IsolationForest(contamination=0.05, random_state=42)
# isolation_forest.fit(scaled_data)

# # Step 5: Predict anomalies
# df['anomaly'] = isolation_forest.predict(scaled_data)

# # Step 6: Identify anomalies (-1 represents anomalies)
# anomalies = df[df['anomaly'] == -1]

# # Display anomalies in the console
# print("Detected Anomalies:")
# print(anomalies)

# # Optionally, save the anomalies to a CSV file
# anomalies.to_csv('detected_anomalies.csv', index=False)
# print("Anomalies saved to 'detected_anomalies.csv'.")


# import pandas as pd
# import re

# # Step 1: Load the CSV data
# file_path = 'firewall_logs.csv'  # Replace with the actual path to your firewall_logs.csv file
# df = pd.read_csv(file_path)

# # Step 2: Preprocess the data
# # Convert timestamp to UNIX format (if necessary)
# df['timestamp'] = pd.to_datetime(df['timestamp'])

# # Step 3: Define valid IP and port ranges
# def is_valid_ip(ip):
#     """ Validate an IP address """
#     # Check if the IP is in the format of 4 octets and the value of each octet is between 0 and 255
#     pattern = re.compile(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
#                          r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
#                          r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
#                          r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
#     return pattern.match(ip) is not None

# def is_valid_port(port):
#     """ Validate port number (should be between 1 and 65535) """
#     return 1 <= port <= 65535

# # Step 4: Detect anomalies based on IP and port validation
# def detect_anomalies(row):
#     ip = row['ip']
#     port = row['port']
    
#     # Check for valid IP
#     if not is_valid_ip(ip):
#         return f"Anomaly Detected: Invalid IP address {ip}."
    
#     # Check for valid port
#     if not is_valid_port(port):
#         return f"Anomaly Detected: Invalid port number {port}."
    
#     return "Log entry is normal."

# # Step 5: Apply anomaly detection on the existing CSV file
# df['anomaly_message'] = df.apply(detect_anomalies, axis=1)

# # Step 6: Filter and display any anomalies detected in the existing data
# anomalies_detected = df[df['anomaly_message'] != "Log entry is normal."]
# if not anomalies_detected.empty:
#     print("Anomalies Detected in the Firewall Logs:")
#     print(anomalies_detected[['timestamp', 'ip', 'port', 'anomaly_message']])
# else:
#     print("No anomalies detected in the firewall logs.")

# # Optionally, save the anomalies to a CSV file for further review
# anomalies_detected.to_csv('detected_anomalies_in_firewall_logs.csv', index=False)



# import pandas as pd
# from sklearn.ensemble import IsolationForest
# from sklearn.preprocessing import LabelEncoder, StandardScaler

# # Step 1: Load the CSV data
# file_path = 'firewall_logs.csv'  # Replace with the actual path to your firewall_logs.csv file
# df = pd.read_csv(file_path)

# # Step 2: Preprocess the data
# # Convert timestamp to UNIX format (if necessary)
# df['timestamp'] = pd.to_datetime(df['timestamp'])

# # Save original port for output purposes
# df['original_port'] = df['port']

# # Encode IP addresses into numeric values using LabelEncoder
# label_encoder_ip = LabelEncoder()
# df['encoded_ip'] = label_encoder_ip.fit_transform(df['ip'])

# # Step 3: Scale the data (but retain original IP and port for later display)
# scaler = StandardScaler()
# scaled_data = scaler.fit_transform(df[['encoded_ip', 'port']])

# # Step 4: Train the Isolation Forest model
# isolation_forest = IsolationForest(contamination=0.05, random_state=42)  # Set contamination rate as 5%
# isolation_forest.fit(scaled_data)

# # Step 5: Predict anomalies
# df['anomaly'] = isolation_forest.predict(scaled_data)

# # Step 6: Label anomalies based on Isolation Forest predictions
# def interpret_anomaly(row):
#     if row['anomaly'] == -1:
#         return "Anomaly Detected: Unusual IP or port."
#     else:
#         return "Log entry is normal."

# df['anomaly_message'] = df.apply(interpret_anomaly, axis=1)

# # Step 7: Filter and display any anomalies detected in the existing data, using original values
# anomalies_detected = df[df['anomaly_message'] != "Log entry is normal."]
# if not anomalies_detected.empty:
#     print("Anomalies Detected in the Firewall Logs:")
#     print(anomalies_detected[['timestamp', 'ip', 'original_port', 'anomaly_message']])
# else:
#     print("No anomalies detected in the firewall logs.")

# # Optionally, save the anomalies to a CSV file for further review
# anomalies_detected[['timestamp', 'ip', 'original_port', 'anomaly_message']].to_csv('detected_anomalies_in_firewall_logs.csv', index=False)


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
