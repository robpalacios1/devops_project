# Dockerfile
# 1. We use an official Python base image
FROM python:3.9-slim

# 2. We set the working directory inside the container
WORKDIR /app

# 3. We copy the dependencies file
COPY requirements.txt .

# 4. We install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. We copy the rest of the app code
COPY . .

# 6. We expose the port on which Flask runs
EXPOSE 5000

# 7. The command to start the application when the container is run
CMD ["python", "app.py"]