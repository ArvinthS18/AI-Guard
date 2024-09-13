# # import pandas as pd
# # from sklearn.model_selection import train_test_split, GridSearchCV, LeaveOneOut
# # from sklearn.ensemble import RandomForestClassifier
# # from sklearn.preprocessing import LabelEncoder

# # # Load user feedback data
# # user_feedback = pd.read_csv('C:/Users/A7765/AI/user_feedback.csv')

# # # Load rules data
# # rules = pd.read_csv('C:/Users/A7765/AI/rules.csv')

# # # Combine IP addresses, traffic types, and actions from both datasets
# # all_ips = pd.concat([user_feedback['ip'], rules['ip']]).unique()
# # all_traffic_types = pd.concat([user_feedback['traffic_type'], rules['traffic_type']]).unique()
# # all_actions = pd.concat([user_feedback['action'], rules['action']]).unique()

# # # Initialize LabelEncoders and fit on combined data
# # ip_encoder = LabelEncoder()
# # traffic_type_encoder = LabelEncoder()
# # action_encoder = LabelEncoder()

# # ip_encoder.fit(all_ips)
# # traffic_type_encoder.fit(all_traffic_types)
# # action_encoder.fit(all_actions)

# # # Encode user feedback data
# # user_feedback['ip'] = ip_encoder.transform(user_feedback['ip'])
# # user_feedback['traffic_type'] = traffic_type_encoder.transform(user_feedback['traffic_type'])
# # user_feedback['action'] = action_encoder.transform(user_feedback['action'])

# # # Split data into features and target
# # X = user_feedback[['ip', 'port', 'traffic_type']]
# # y = user_feedback['action']

# # # Split data into training and testing sets
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # # Hyperparameter tuning for RandomForestClassifier using Leave-One-Out cross-validation
# # param_grid = {
# #     'n_estimators': [100, 200],
# #     'max_features': ['auto', 'sqrt'],
# #     'max_depth': [10, 20, None],
# #     'criterion': ['gini', 'entropy']
# # }

# # # Use Leave-One-Out cross-validation
# # loo = LeaveOneOut()

# # # Grid Search
# # grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42),
# #                            param_grid=param_grid,
# #                            cv=loo,
# #                            n_jobs=-1,
# #                            verbose=2)

# # grid_search.fit(X_train, y_train)

# # # Best model from Grid Search
# # best_model = grid_search.best_estimator_

# # # Train the best model on the full training data
# # best_model.fit(X_train, y_train)

# # # Encode rules data
# # rules['ip'] = ip_encoder.transform(rules['ip'])
# # rules['traffic_type'] = traffic_type_encoder.transform(rules['traffic_type'])
# # # No need to encode rules['action'] here since it will be replaced by the prediction

# # # Predict actions for rules
# # rules_X = rules[['ip', 'port', 'traffic_type']]
# # rules['predicted_action'] = best_model.predict(rules_X)

# # # Decode the labels back to original values
# # rules['ip'] = ip_encoder.inverse_transform(rules['ip'])
# # rules['traffic_type'] = traffic_type_encoder.inverse_transform(rules['traffic_type'])
# # rules['predicted_action'] = action_encoder.inverse_transform(rules['predicted_action'])

# # # Debug: Print the predicted actions
# # print("Predicted actions:")
# # print(rules[['ip', 'port', 'traffic_type', 'predicted_action']])

# # # Update the action in rules based on the prediction
# # rules['action'] = rules['predicted_action']
# # rules.drop(columns=['predicted_action'], inplace=True)

# # # Debug: Print the updated rules before saving
# # print("Updated rules:")
# # print(rules)

# # # Save the updated rules
# # rules.to_csv('C:/Users/A7765/AI/rules.csv', index=False)

# # print("Rules have been updated successfully.")

# import pandas as pd
# from sklearn.model_selection import LeaveOneOut, GridSearchCV
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder

# # Load user feedback data
# user_feedback = pd.read_csv('C:/Users/A7765/AI/user_feedback.csv')

# # Load rules data
# rules = pd.read_csv('C:/Users/A7765/AI/rules.csv')

# # Combine IP addresses, traffic types, and actions from both datasets
# all_ips = pd.concat([user_feedback['ip'], rules['ip']]).unique()
# all_traffic_types = pd.concat([user_feedback['traffic_type'], rules['traffic_type']]).unique()
# all_actions = pd.concat([user_feedback['action'], rules['action']]).unique()

# # Initialize LabelEncoders and fit on combined data
# ip_encoder = LabelEncoder()
# traffic_type_encoder = LabelEncoder()
# action_encoder = LabelEncoder()

# ip_encoder.fit(all_ips)
# traffic_type_encoder.fit(all_traffic_types)
# action_encoder.fit(all_actions)

# # Encode user feedback data
# user_feedback['ip'] = ip_encoder.transform(user_feedback['ip'])
# user_feedback['traffic_type'] = traffic_type_encoder.transform(user_feedback['traffic_type'])
# user_feedback['action'] = action_encoder.transform(user_feedback['action'])

# # Split data into features and target
# X = user_feedback[['ip', 'port', 'traffic_type']]
# y = user_feedback['action']

# # Hyperparameter tuning for RandomForestClassifier using Leave-One-Out cross-validation
# param_grid = {
#     'n_estimators': [100, 200],
#     'max_features': ['auto', 'sqrt'],
#     'max_depth': [10, 20, None],
#     'criterion': ['gini', 'entropy']
# }

# # Use LeaveOneOut cross-validation
# loo = LeaveOneOut()

# # Grid Search with LeaveOneOut CV
# grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42),
#                            param_grid=param_grid,
#                            cv=loo,
#                            n_jobs=-1,
#                            verbose=2)

# # Fit the grid search
# grid_search.fit(X, y)

# # Best model from Grid Search
# best_model = grid_search.best_estimator_

# # Encode rules data
# rules['ip'] = ip_encoder.transform(rules['ip'])
# rules['traffic_type'] = traffic_type_encoder.transform(rules['traffic_type'])
# # No need to encode rules['action'] here since it will be replaced by the prediction

# # Predict actions for rules
# rules_X = rules[['ip', 'port', 'traffic_type']]
# rules['predicted_action'] = best_model.predict(rules_X)

# # Decode the labels back to original values
# rules['ip'] = ip_encoder.inverse_transform(rules['ip'])
# rules['traffic_type'] = traffic_type_encoder.inverse_transform(rules['traffic_type'])
# rules['predicted_action'] = action_encoder.inverse_transform(rules['predicted_action'])

# # Debug: Print the predicted actions
# print("Predicted actions:")
# print(rules[['ip', 'port', 'traffic_type', 'predicted_action']])

# # Update the action in rules based on the prediction
# rules['action'] = rules['predicted_action']
# rules.drop(columns=['predicted_action'], inplace=True)

# # Debug: Print the updated rules before saving
# print("Updated rules:")
# print(rules)

# # Save the updated rules
# rules.to_csv('C:/Users/A7765/AI/rules.csv', index=False)

# print("Rules have been updated successfully.")
import pandas as pd
from sklearn.model_selection import LeaveOneOut, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load user feedback data
user_feedback = pd.read_csv('C:/Users/A7765/AI/user_feedback.csv')

# Load rules data
rules = pd.read_csv('C:/Users/A7765/AI/rules.csv')

# Combine IP addresses, traffic types, and actions from both datasets
all_ips = pd.concat([user_feedback['ip'], rules['ip']]).unique()
all_traffic_types = pd.concat([user_feedback['traffic_type'], rules['traffic_type']]).unique()
all_actions = pd.concat([user_feedback['action'], rules['action']]).unique()

# Initialize LabelEncoders and fit on combined data
ip_encoder = LabelEncoder()
traffic_type_encoder = LabelEncoder()
action_encoder = LabelEncoder()

ip_encoder.fit(all_ips)
traffic_type_encoder.fit(all_traffic_types)
action_encoder.fit(all_actions)

# Encode user feedback data
user_feedback['ip'] = ip_encoder.transform(user_feedback['ip'])
user_feedback['traffic_type'] = traffic_type_encoder.transform(user_feedback['traffic_type'])
user_feedback['action'] = action_encoder.transform(user_feedback['action'])

# Split data into features and target
X = user_feedback[['ip', 'port', 'traffic_type']]
y = user_feedback['action']

# Hyperparameter tuning for RandomForestClassifier using Leave-One-Out cross-validation
param_grid = {
    'n_estimators': [100, 200],
    'max_features': ['sqrt', 'log2'],  # Remove 'auto' since it's invalid in recent sklearn versions
    'max_depth': [10, 20, None],
    'criterion': ['gini', 'entropy']
}

# Use LeaveOneOut cross-validation
loo = LeaveOneOut()

# Grid Search with LeaveOneOut CV
grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42),
                           param_grid=param_grid,
                           cv=loo,
                           n_jobs=-1,
                           verbose=2)

# Fit the grid search
grid_search.fit(X, y)

# Best model from Grid Search
best_model = grid_search.best_estimator_

# Encode rules data
rules['ip'] = ip_encoder.transform(rules['ip'])
rules['traffic_type'] = traffic_type_encoder.transform(rules['traffic_type'])

# Predict actions for rules
rules_X = rules[['ip', 'port', 'traffic_type']]
rules['predicted_action'] = best_model.predict(rules_X)

# Decode the labels back to original values
rules['ip'] = ip_encoder.inverse_transform(rules['ip'])
rules['traffic_type'] = traffic_type_encoder.inverse_transform(rules['traffic_type'])
rules['predicted_action'] = action_encoder.inverse_transform(rules['predicted_action'])

# Debug: Print the predicted actions
print("Predicted actions:")
print(rules[['ip', 'port', 'traffic_type', 'predicted_action']])

# Update the action in rules based on the prediction
rules['action'] = rules['predicted_action']
rules.drop(columns=['predicted_action'], inplace=True)

# Save the updated rules
rules.to_csv('C:/Users/A7765/AI/rules.csv', index=False)

print("Rules have been updated successfully.")

# -------- Breach Detection Logic ---------

# Load the logs data for breach detection
log_file = r'C:\Users\A7765\AI\firewall_logs.csv'
logs = pd.read_csv(log_file)

# Strip any extra whitespace from column names
logs.columns = logs.columns.str.strip()

# Convert 'timestamp' to datetime
logs['timestamp'] = pd.to_datetime(logs['timestamp'], errors='coerce', format='%Y-%m-%d %H:%M:%S')

# Drop rows with invalid timestamps
logs = logs.dropna(subset=['timestamp'])

# Encode 'ip' and 'traffic_type' using the same encoders as used in training
logs['ip'] = ip_encoder.transform(logs['ip'])
logs['traffic_type'] = traffic_type_encoder.transform(logs['traffic_type'])

# Apply the RandomForestClassifier to predict the 'action'
logs_X = logs[['ip', 'port', 'traffic_type']]
logs['predicted_action'] = best_model.predict(logs_X)

# Compare actual 'action' with 'predicted_action' and flag discrepancies
logs['breach_detected'] = logs['action'] != logs['predicted_action']

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

# Detect breaches based on the predicted actions
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

# Inform the user about discrepancies (if any)
if logs['breach_detected'].any():
    print("\nBreach detected based on model prediction.")
    print(logs[logs['breach_detected']][['ip', 'port', 'traffic_type', 'action', 'predicted_action']])
else:
    print("No breaches detected by the model.")
