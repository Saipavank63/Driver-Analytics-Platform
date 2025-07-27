import joblib
import pandas as pd

model = joblib.load("model/driver_risk_model.pkl")


def score_driver(data: pd.DataFrame) -> pd.DataFrame:
    data['risk_score'] = model.predict_proba(
        data)[:, 1]  # Assume 1 is high risk
    return data
