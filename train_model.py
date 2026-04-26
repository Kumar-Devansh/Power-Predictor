import pandas as pd
import numpy as np
import pickle
import os

input_path = "household_power_consumption.txt"

print("Reading and sampling dataset...")
data = []
with open(input_path, 'r') as f:
    header = f.readline().strip().split(';')
    # We will sample every 100th row to keep training fast
    for i, line in enumerate(f):
        if i % 100 == 0:
            row = line.strip().split(';')
            if '?' not in row: # drop na
                data.append(row)

df = pd.DataFrame(data, columns=header)
df['Global_active_power'] = pd.to_numeric(df['Global_active_power'])

# Parse Date and extract day/month
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['day'] = df['Date'].dt.day
df['month'] = df['Date'].dt.month

# Extract hour from Time
df['hour_of_day'] = df['Time'].apply(lambda x: int(x.split(':')[0]))

# Create synthetic 'total_load' feature mimicking user's deterministic watt calculation
# Assuming user's total_load in Watts correlate roughly to active power * 1000 with some noise
np.random.seed(42)
df['total_load'] = df['Global_active_power'] * 1000 * np.random.uniform(0.8, 1.2, size=len(df))

X = df[['total_load', 'hour_of_day', 'day', 'month']]
y = df['Global_active_power']

try:
    import xgboost as xgb
    model = xgb.XGBRegressor(n_estimators=100, random_state=42)
    print("Training XGBoost Regressor...")
except ImportError:
    from sklearn.ensemble import RandomForestRegressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    print("Training Random Forest Regressor (XGBoost not available)...")

model.fit(X, y)

os.makedirs('model', exist_ok=True)
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)
    
print("Model trained and saved to model/model.pkl successfully!")
