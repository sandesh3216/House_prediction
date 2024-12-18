
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY flask_Api.py .
COPY linear_regression_model.pkl .
COPY templates/ ./templates/
COPY static/ ./static/


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "flask_Api.py"]
