# CRM-Intelligence
# 📊 CRM Intelligence Machine

An end-to-end **CRM Intelligence system** that leverages **Machine Learning and NLP** to analyze customer interactions and predict:

- 🔹 **Customer Interest** (from conversation text – NLP)
- 🔹 **Lead Conversion Probability** (from structured/tabular data)

This project demonstrates a real-world **ML pipeline + API + UI** workflow suitable for production-ready CRM analytics.

---

## 🚀 Project Overview

Customer Relationship Management (CRM) teams deal with large volumes of leads and conversations.  
This project helps automate decision-making by answering:

- Is a lead **interested or not** based on conversation text?
- What is the **probability of conversion** for a lead?
- How can CRM teams **prioritize leads intelligently**?

The solution combines **NLP models, tabular ML models, FastAPI backend, and Streamlit UI**.

---

## 🧠 Machine Learning Tasks

### 🔹 Task 1: Interest Detection (NLP)
- Input: Lead conversation / status text
- Model: NLP pipeline (TF-IDF + ML classifier)
- Output:
  - Interested / Not Interested
  - Confidence score

### 🔹 Task 2: Conversion Prediction (Tabular ML)
- Input features:
  - Location
  - Business Executive
  - Text length (engineered feature)
- Output:
  - Converted / Not Converted
  - Probability scores

---

## 🗂️ Project Structure

```text
├── app.py                      # FastAPI backend (prediction API)
├── UI.py                       # Streamlit UI for live predictions
├── Data_cleaning_and_EDA.ipynb # Data cleaning & exploratory analysis
├── NLP.ipynb                   # NLP model training & evaluation
├── Tabular.ipynb               # Tabular ML model training
├── nlp_pipeline.pkl            # Saved NLP model
├── task2_tabular_clf.pkl       # Saved tabular model
├── requirements.txt            # Project dependencies
├── dockerfile                  # Docker configuration
└── README.md                   # Project documentation

## Input
{
  "status_information": "Customer is interested and asked for pricing",
  "location": "Hyderabad",
  "executive": "Prema"
}


## Output
{
  "Task1_NLP": {
    "label": "Interested",
    "confidence": 0.92
  },
  "Task2_Tabular": {
    "prediction": "Converted",
    "probabilities": {
      "Not Converted": 0.25,
      "Converted": 0.75
    }
  }
}
