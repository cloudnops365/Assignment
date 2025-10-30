# Step 1: Use an official Python runtime as base image
FROM python:3.11-slim

# Step 2: Set working directory in container
WORKDIR /app

# Step 3: Copy app files
COPY . /app

# Step 4: Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn prometheus-client

# Step 5: Expose port
EXPOSE 8000

# Step 6: Run FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

