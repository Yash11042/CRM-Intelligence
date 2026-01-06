# =========================
# Dockerfile
# =========================

# Step 1: Use Python base image
FROM python:3.11-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy files
COPY requirements.txt .
COPY 1000\ leads.xlsx .
COPY data_prep_and_training.py .
COPY app_fastapi.py .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Train models
RUN python data_prep_and_training.py

# Step 6: Expose FastAPI port
EXPOSE 8000

# Step 7: Run FastAPI app
CMD ["uvicorn", "app_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
