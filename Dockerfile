# Step 1: Use a computer that already has Python 3.11 installed
FROM python:3.11-slim

# Step 2: Create a folder called 'app' to hold our work
WORKDIR /app

# Step 3: Copy the 'Shopping List' and install the items on it
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy your 'main.py' logic into the folder
COPY main.py .

# Step 5: Tell the computer to start the web server on Port 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
