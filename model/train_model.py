import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Dummy data - replace with Delta Lake read logic
df = pd.read_csv('driver_features.csv')
X = df.drop(columns=["risk_label"])
y = df["risk_label"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model/driver_risk_model.pkl")
print("Model saved.")
