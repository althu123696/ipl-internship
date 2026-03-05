import os
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from prometheus_client import Gauge
from prometheus_fastapi_instrumentator import Instrumentator

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ipl_backend")

app = FastAPI(title="IPL Runs Prediction", version="1.0")

# Load trained model once at startup, with error handling
try:
    model = joblib.load("model/poly_linear_regression_pipeline.pkl")
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Model failed to load: {e}")
    raise RuntimeError("Model could not be loaded.")

# Prometheus instrumentation
Instrumentator().instrument(app).expose(app)

# Custom metric for leakage gap
leakage_metric = Gauge("data_leakage_gap", "Gap between train and test R2")

def log_leakage_gap(train_score: float, test_score: float):
    """Log real leakage gap from training pipeline."""
    gap = train_score - test_score
    leakage_metric.set(gap)
    logger.info(f"Leakage gap logged: {gap}")

class PlayerData(BaseModel):
    Inns: int
    NO: int
    Avg: float
    BF: int
    four_runs: int = Field(..., alias="4s")
    six_runs: int = Field(..., alias="6s")

@app.get("/")
def root():
    return {"message": "IPL API is running"}

@app.post("/predict")
def predict_runs(player: PlayerData):
    try:
        df = pd.DataFrame([player.dict(by_alias=True)])
        prediction = model.predict(df)[0]
        return {"Predicted Runs": round(float(prediction), 0)}
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise HTTPException(status_code=500, detail="Prediction error")

# Only enable simulation in development mode
if os.getenv("DEBUG", "false").lower() == "true":
    @app.get("/simulate_leakage/{gap_value}")
    def simulate_leakage(gap_value: float):
        leakage_metric.set(gap_value)
        logger.warning(f"Simulated leakage gap set to {gap_value}")
        return {"message": f"Leakage gap set to {gap_value}"}
