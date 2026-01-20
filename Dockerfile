FROM python:3.9-slim

WORKDIR /app

# Copy files
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY rf_model.pkl rf_model.pkl
COPY labeled_nutrition_data.csv labeled_nutrition_data.csv

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Gradio
EXPOSE 7860

# Run the application
CMD ["python", "app.py"]
