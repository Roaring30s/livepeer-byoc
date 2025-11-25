FROM python:3.11-slim

RUN pip install flask

WORKDIR /app

COPY pulse_server.py .

EXPOSE 5000

CMD ["python", "pulse_server.py"]

