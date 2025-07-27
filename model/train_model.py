import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load sample feature data
df = pd.read_csv("driver_features.csv")
X = df[["speed", "acceleration", "harsh_braking", "aggressive_steering"]]
y = df["incident_risk"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "driver_risk_model.pkl")
