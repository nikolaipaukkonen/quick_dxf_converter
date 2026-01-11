FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

# Default command (override at runtime if needed)
CMD ["python", "converter.py", "example.TXT", "out.dxf"]
