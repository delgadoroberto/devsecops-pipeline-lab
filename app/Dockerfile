# Step 1: Use an official lightweight Python image
FROM python:3.10-slim

# Step 2: Set working directory
WORKDIR /usr/src/app

# Step 3: Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy application source code
COPY src/ ./src

# Step 5: Expose application port
EXPOSE 5000

# Security Note: Running as root intentionally for initial lab compliance testing.
# A standard hardening practice would involve adding a non-root user here.

# Step 6: Define the command to run the app
CMD ["python", "src/app.py"]
