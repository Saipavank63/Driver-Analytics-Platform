import os

# === Data Paths ===
RAW_TELEMETRY_PATH = os.getenv(
    "RAW_TELEMETRY_PATH", "data/raw/telemetry_data.json")
DELTA_FEATURE_PATH = os.getenv(
    "DELTA_FEATURE_PATH", "/driver_analytics/delta/telemetry_features")
MODEL_PATH = os.getenv("MODEL_PATH", "models/driver_risk_model.pkl")
DRIVER_SCORES_PATH = os.getenv(
    "DRIVER_SCORES_PATH", "data/processed/driver_scores.csv")

# === Stream / Kafka Settings (if applicable) ===
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "telemetry-stream")
KAFKA_BOOTSTRAP_SERVERS = os.getenv(
    "KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

# === AWS Settings (optional if deployed) ===
AWS_REGION = os.getenv("AWS_REGION", "us-west-2")
S3_BUCKET = os.getenv("S3_BUCKET", "driver-analytics-data")

# === Application Settings ===
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
# For classifying high-risk drivers
MODEL_THRESHOLD = float(os.getenv("MODEL_THRESHOLD", 0.7))
