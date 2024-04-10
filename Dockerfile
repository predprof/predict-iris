FROM python:3.9-slim-buster

COPY *.py /app/
COPY requirements.txt /app/

WORKDIR /app/

RUN pip install -r requirements.txt

RUN python train.py

# Expose the port uvicorn is running on
EXPOSE 80

# Run uvicorn server
CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
