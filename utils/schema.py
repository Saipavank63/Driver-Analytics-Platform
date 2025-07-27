from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Location(BaseModel):
    lat: float = Field(..., description="Latitude of the vehicle")
    lon: float = Field(..., description="Longitude of the vehicle")


class TelemetryRecord(BaseModel):
    vehicle_id: str = Field(..., description="Unique vehicle identifier")
    timestamp: datetime = Field(..., description="ISO 8601 timestamp")
    speed: float = Field(..., ge=0, description="Vehicle speed in km/h")
    acceleration: float = Field(..., description="Acceleration in m/s²")
    steering_angle: float = Field(..., description="Steering angle in degrees")
    brake_status: int = Field(..., description="1 if braking, else 0")
    location: Location


class FeatureRecord(BaseModel):
    vehicle_id: str
    timestamp: datetime
    speed: float
    acceleration: float
    steering_angle: float
    harsh_braking: int
    aggressive_steering: int
    risk_score: Optional[float] = None  # output of ML model
