# Use an official Python runtime as a parent image
FROM python:3.10-slim
# Set the working directory in the container
WORKDIR /app
# Copy the requirements file into the container at /app
COPY requirements.txt /app/
# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy all Python files from the host's current folder into the container's
COPY . /app/
CMD [ "python", "run.py" ]
