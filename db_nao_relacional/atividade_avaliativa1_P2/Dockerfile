
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN python -m pip install --upgrade pip

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy application code
COPY app /app/app

# Expose port used by the FastAPI app
EXPOSE 8005

# Run uvicorn using the package path
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8005", "--reload"]