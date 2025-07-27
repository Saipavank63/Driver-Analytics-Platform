import time
import json
import random
from pyspark.sql import SparkSession
from datetime import datetime

spark = SparkSession.builder \
    .appName("TelemetryStreamIngestion") \
    .getOrCreate()


def mock_telemetry():
    return {
        "driver_id": random.randint(1000, 1100),
        "speed": random.uniform(30, 120),
        "brake_pressure": random.uniform(0, 1),
        "acceleration": random.uniform(-2, 3),
        "timestamp": datetime.utcnow().isoformat()
    }


while True:
    telemetry = [mock_telemetry() for _ in range(10)]
    df = spark.createDataFrame(telemetry)
    df.write.format("delta").mode("append").save("/tmp/delta/telemetry")
    print("Telemetry batch saved.")
    time.sleep(5)
