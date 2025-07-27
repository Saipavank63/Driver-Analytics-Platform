SELECT
    driver_id,
    AVG(speed) AS avg_speed,
    MAX(speed) AS max_speed,
    STDDEV(speed) AS speed_volatility,
    AVG(brake_pressure) AS avg_brake,
    AVG(acceleration) AS avg_accel
FROM {{ ref('raw_telemetry') }}
GROUP BY driver_id
