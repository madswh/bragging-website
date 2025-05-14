#python environment
FROM python:3.12-slim
# Set the working directory
WORKDIR /bragging-website
# Copy the directory contents into the container at /bragging-website
COPY . /bragging-website
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Expose port 5000 for the Flask app
EXPOSE 5001

CMD [ "python3", "app.py" ]
