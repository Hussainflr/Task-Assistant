FROM python:3.11-slim

WORKDIR /app

# -------------------------
# Install system dependencies
# -------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# -------------------------
# Copy files
# -------------------------
COPY requirements.txt .

# Upgrade pip first
RUN pip install --upgrade pip

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of app
COPY . .

# Expose Streamlit port
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]