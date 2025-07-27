from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from model.inference import score_driver


def extract_features():
    df = pd.read_parquet("/tmp/delta/telemetry")
    df.to_csv("/tmp/processed_features.csv")


def score():
    df = pd.read_csv("/tmp/processed_features.csv")
    scored = score_driver(df)
    scored.to_csv("/tmp/scored_data.csv", index=False)


with DAG("driver_risk_pipeline", start_date=datetime(2025, 1, 1), schedule_interval="@hourly", catchup=False) as dag:
    extract = PythonOperator(task_id="extract_features",
                             python_callable=extract_features)
    risk_score = PythonOperator(task_id="score_driver", python_callable=score)

    extract >> risk_score
