FROM python:3.11-slim

WORKDIR /app
COPY . .

# Install system deps (optional, keep it light)
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

