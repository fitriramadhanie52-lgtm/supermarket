FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy app
COPY supermarket.py .

# Expose port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "supermarket.py", "--server.port=8501", "--server.address=0.0.0.0"]
