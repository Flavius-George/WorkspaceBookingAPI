FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app .

CMD ["fastapi", "run", "main.py" , "--host", "192.168.50.214", "--port", "8888"]

