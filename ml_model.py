import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, LeaveOneOut
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

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hyperparameter tuning for RandomForestClassifier using Leave-One-Out cross-validation
param_grid = {
    'n_estimators': [100, 200],
    'max_features': ['auto', 'sqrt'],
    'max_depth': [10, 20, None],
    'criterion': ['gini', 'entropy']
}

# Use Leave-One-Out cross-validation
loo = LeaveOneOut()

# Grid Search
grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42),
                           param_grid=param_grid,
                           cv=loo,
                           n_jobs=-1,
                           verbose=2)

grid_search.fit(X_train, y_train)

# Best model from Grid Search
best_model = grid_search.best_estimator_

# Train the best model on the full training data
best_model.fit(X_train, y_train)

# Encode rules data
rules['ip'] = ip_encoder.transform(rules['ip'])
rules['traffic_type'] = traffic_type_encoder.transform(rules['traffic_type'])
# No need to encode rules['action'] here since it will be replaced by the prediction

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

# Debug: Print the updated rules before saving
print("Updated rules:")
print(rules)

# Save the updated rules
rules.to_csv('C:/Users/A7765/AI/rules.csv', index=False)

print("Rules have been updated successfully.")
