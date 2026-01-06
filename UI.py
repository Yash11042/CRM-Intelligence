# app_streamlit.py
import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="CRM Intelligence Demo")

st.title("CRM Intelligence — Task1 (NLP) + Task2 (Tabular) demo")

# Load models
@st.cache(allow_output_mutation=True)
def load_models():
    with open('nlp_pipeline.pkl','rb') as f:
        task1 = pickle.load(f)
    with open('task2_tabular_clf.pkl','rb') as f:
        task2 = pickle.load(f)
    return task1, task2

task1_model, task2_model = load_models()

st.header("Single lead prediction")
lead_name = st.text_input("Lead Name")
location = st.text_input("Location (e.g., hyderabad)")
executive = st.text_input("Executive (e.g., Prema)")
status_info = st.text_area("Status information / conversation text")

if st.button("Predict"):
    # Task1
    text = status_info if status_info else ""
    t_pred = task1_model.predict([text])[0]
    t_prob = task1_model.predict_proba([text])[0]

    # Task2: craft dataframe row with text_len
    row = pd.DataFrame([{
        'Location': location if location else 'Unknown',
        'business_executive': executive.title() if executive else 'Unknown',
        'text_len': len(text)
    }])
    conv_pred = task2_model.predict(row)[0]
    conv_proba = task2_model.predict_proba(row)[0]

    st.subheader("Task 1 — Interest detection (from conversation)")
    st.write("Predicted label:", "Interested" if t_pred==1 else "Not Interested")
    st.write("Probabilities:", dict(zip(task1_model.classes_, [float(x) for x in t_prob])))

    st.subheader("Task 2 — Conversion prediction (from location/executive)")
    st.write("Predicted label:", "Converted" if conv_pred==1 else "Not Converted")
    st.write("Probabilities:", conv_proba.tolist())
