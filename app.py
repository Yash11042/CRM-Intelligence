
# =========================
# app_fastapi.py
# =========================
from fastapi import FastAPI
from pydantic import BaseModel
import random

# Initialize the FastAPI app
app = FastAPI(
    title="CRM Intelligence API",
    description="Simple FastAPI for Interest (NLP) and Conversion (Tabular) Prediction",
    version="1.0.0"
)

# ----------------------------
# Define Input Schema
# ----------------------------
class LeadInput(BaseModel):
    status_information: str
    location: str = "Unknown"
    executive: str = "Unknown"

# ----------------------------
# Root Route
# ----------------------------
@app.get("/")
def home():
    return {"message": "Welcome to the CRM Intelligence FastAPI!"}

# ----------------------------
# Predict Route
# ----------------------------
@app.post("/predict")
def predict(lead: LeadInput):
    """
    Predict Interest (Task 1 - NLP)
    and Conversion (Task 2 - Tabular)
    """

    # ----- Dummy logic for now -----
    # You can replace this later with your trained models.
    nlp_label = "Interested" if "interested" in lead.status_information.lower() else "Not Interested"
    nlp_confidence = round(random.uniform(0.7, 0.99), 3)

    converted = random.choice([0, 1])
    tab_pred = "Converted" if converted == 1 else "Not Converted"
    tab_probs = {"Not Converted": round(random.uniform(0.1, 0.6), 2),
                 "Converted": round(random.uniform(0.4, 0.9), 2)}

    return {
        "Task1_NLP": {
            "label": nlp_label,
            "confidence": nlp_confidence
        },
        "Task2_Tabular": {
            "prediction": tab_pred,
            "probabilities": tab_probs
        }
    }

