import pandas as pd
from sklearn.ensemble import IsolationForest

# Load the log data from a CSV file
df = pd.read_csv('firewall_logs.csv')

# Converting timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Encoding categorical variables
df['traffic_type'] = df['traffic_type'].astype('category').cat.codes
df['ip'] = df['ip'].astype('category').cat.codes

# Selecting features for anomaly detection
features = ['ip', 'port', 'traffic_type']

# Applying Isolation Forest for anomaly detection
model = IsolationForest(contamination=0.1, random_state=42)
df['anomaly'] = model.fit_predict(df[features])

# Identifying and displaying anomalies
anomalies = df[df['anomaly'] == -1]

# Save anomalies to a CSV file
anomalies.to_csv('anomalies_detected.csv', index=False)

print("Anomalies detected and saved to 'anomalies_detected.csv'")
