FROM python:3.11-slim

# Install build tools and Cairo dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libcairo2-dev \
    tesseract-ocr \
    libtesseract-dev \
    pkg-config \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "run.py"]
