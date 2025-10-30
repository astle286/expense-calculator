# Use official Python slim image
FROM python:3.11-slim

# Install build tools and OCR dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libcairo2-dev \
    tesseract-ocr \
    libtesseract-dev \
    pkg-config \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependency file and install Python packages
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "run.py"]
